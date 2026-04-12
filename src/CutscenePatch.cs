using UnityEngine;
using UnityEngine.SceneManagement;
using Utils;
using View.Cutscenes;

namespace TerraNilAP;

public class CutscenePatch : UnityEngine.MonoBehaviour
{
    private void Awake()
    {
        Object.DontDestroyOnLoad(this.gameObject);
        SceneManager.activeSceneChanged += delegate (Scene current, Scene next)
        {
            if (next.name == "Main")
            {
                MonoSingleton<CutsceneHandler>.Instance.EndOfIntroCutscene();
            }
        };
    }
}
