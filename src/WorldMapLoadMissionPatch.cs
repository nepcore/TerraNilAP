using Data;
using Global;
using HarmonyLib;
using System.Reflection;
using UnityEngine.EventSystems;
using UnityEngine.UI;
using Utils;
using View.Handlers;
using WorldMap.UiHelpers;

namespace TerraNilAP;

[HarmonyPatch(typeof(MissionInfoPopup), "Populate")]
class WorldMapLoadMissionPatch
{
    public static void Postfix(MissionData __0, MissionInfoPopup __instance)
    {
        var mission = (int) __0.mission;
        var platform = MonoSingleton<CampaignStateManager>.Instance.Platform;
        var btn = (Button) __instance.GetType().GetField("mainButton", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(__instance);
        var orig = btn.onClick;
        btn.onClick = new();
        btn.onClick.AddListener(() => {
            if (platform.FileExists<Model.State.GameState>($"{mission}_autosave.save", platform.SavesDirectory))
            {
                var savePath = System.IO.Path.Combine(platform.SavesDirectory, $"{mission}_autosave.save");
                EventSystem.current.SetSelectedGameObject(null);
                string text = MonoSingleton<CampaignStateManager>.Instance.LoadGameState(savePath);
                if (text != string.Empty)
                {
                    MonoSingleton<MessageHandler>.Instance.CreateConfirmationDialog(
                        "Ui.Basics.ErrorTitle",
                        "Ui.Basics.LoadError",
                        text
                    );
                }
            }
            else
            {
                orig.Invoke();
            }
        });
    }
}
