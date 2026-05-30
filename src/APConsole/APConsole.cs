using Archipelago.MultiClient.Net.MessageLog.Messages;
using System;
using System.Linq;
using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;

namespace APConsole;

public class APConsole
{
    private class ConsoleUpdate : MonoBehaviour
    {
        private APConsole self;

        public void SetConsole(APConsole console)
        {
            self = console;
        }

        private void Update()
        {
            self.Update();
        }
    }

    private GameObject console;
    private TextMeshProUGUI consoleText;
    private string history;
    private Func<Scene, Scene, bool> shouldRender;
    private AssetBundle AssetBundle;
    private TMP_FontAsset Font;
    private bool visible = true;
    private Queue queue = new();

    public APConsole(
        AssetBundle assetBundle,
        Func<Scene, Scene, bool> renderConsoleInScene = null
    )
    {
        renderConsoleInScene ??= (_, _) => true;
        shouldRender = renderConsoleInScene;
        AssetBundle = assetBundle;
        SetupConsole();
        SceneManager.activeSceneChanged += OnSceneChanged;
    }

    private void OnSceneChanged(Scene from, Scene to)
    {
        if (shouldRender(from, to)) SetupConsole();
    }

    private void SetupConsole()
    {
        if (console != null) GameObject.DestroyImmediate(console);
        console = GameObject.Instantiate(AssetBundle.LoadAsset<GameObject>("APConsole"));
        console.AddComponent<ConsoleUpdate>().SetConsole(this);
        console.SetActive(visible);

        consoleText = console.transform.Find("Scroll View/Viewport/Content").gameObject.AddComponent<TextMeshProUGUI>();
        if (history != null) consoleText.text = history;
        if (Font != null) consoleText.font = Font;
        consoleText.fontSize = 24;
        consoleText.paragraphSpacing = 25;
        consoleText.margin = new (8, 8, 8, 8);
    }

    public void SetFont(TMP_FontAsset font)
    {
        Font = font;
        consoleText.font = font;
    }

    public void ToggleVisible()
    {
        visible = !visible;
        if (console != null) console.SetActive(visible);
    }

    private void Update()
    {
        if (queue.Count != 0)
        {
            while (queue.Count != 0)
            {
                var msg = queue.Dequeue();
                history += $"\n{msg}";
            }

            if (consoleText != null) consoleText.text = history;
        }
    }

    public void AddText(string msg)
    {
        queue.Enqueue(msg);
    }

    public void AddAPMessage(LogMessage msg)
    {
        var colorizedParts = msg.Parts.Select(part => {
            if (part.IsBackgroundColor) return part.Text;
            var c = part.Color;
            var hex = $"{c.R:X2}{c.G:X2}{c.B:X2}";
            if (hex == "008000") hex = "44C444";
            return $"<color=#{hex}>{part.Text}</color>";
        });
        AddText(string.Join("", colorizedParts));
    }

    public void Destroy()
    {
        SceneManager.activeSceneChanged -= OnSceneChanged;
        if (console != null) GameObject.DestroyImmediate(console);
    }
}
