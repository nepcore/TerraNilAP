using HarmonyLib;
using Menus;
using System.Reflection;
using UnityEngine.UI;

namespace TerraNilAP;

[HarmonyPatch(typeof(PauseMenu), "Show")]
class PauseMenuPatch
{
    public static void Postfix(PauseMenu __instance)
    {
        if (UnityEngine.SceneManagement.SceneManager.GetActiveScene().name == "Main")
        {
            TerraNilAP.Logger.LogInfo("Enabling WorldMap Button");
            var worldMapBtn = (Button)__instance
                .GetType()
                .GetField("returnToWorldMapButton", BindingFlags.Instance | BindingFlags.NonPublic)
                .GetValue(__instance);
            worldMapBtn.gameObject.SetActive(true);
            worldMapBtn.onClick = new();
            worldMapBtn.onClick.AddListener(__instance.ConfirmWorldMap);
            var restartMapBtn = (Button)__instance
                .GetType()
                .GetField("restartMapButton", BindingFlags.Instance | BindingFlags.NonPublic)
                .GetValue(__instance);
            restartMapBtn.gameObject.SetActive(true);
            var restartTierBtn = (Button)__instance
                .GetType()
                .GetField("restartTierButton", BindingFlags.Instance | BindingFlags.NonPublic)
                .GetValue(__instance);
            restartTierBtn.gameObject.SetActive(true);
        }
    }
}
