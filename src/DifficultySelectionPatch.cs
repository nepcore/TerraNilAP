using HarmonyLib;
using Settings.Difficulty;
using System.Collections.Generic;
using System.Reflection;
using Utils;
using View.UiHelpers.Panels;

namespace TerraNilAP;

[HarmonyPatch(typeof(View.UiHelpers.Panels.DifficultySelectPanel), "Start")]
class DifficultySelectionPatch
{
    public static int Difficulty = 2;

    public static void Postfix()
    {
        TerraNilAP.Logger.LogInfo("Difficulty panel awake");
        var dsp = MonoSingleton<DifficultySelectPanel>.Instance;
        var presets = (List<DifficultySettingsObject>)dsp
            .GetType()
            .GetField("presets", BindingFlags.Instance | BindingFlags.NonPublic)
            .GetValue(dsp);
        dsp
            .GetType()
            .GetField("_chosenDifficulty", BindingFlags.Instance | BindingFlags.NonPublic)
            .SetValue(dsp, presets[Difficulty]);
        dsp.PressConfirmButton();
        TerraNilAP.Logger.LogInfo("Difficulty configured");
    }
}
