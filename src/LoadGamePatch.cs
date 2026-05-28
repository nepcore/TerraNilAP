using Global;
using HarmonyLib;
using System;
using System.IO;
using System.Text.RegularExpressions;

namespace TerraNilAP;

[HarmonyPatch(typeof(CampaignStateManager), "LoadGameState")]
class LoadGamePatch
{
    public static bool Prefix(ref string __0, CampaignStateManager __instance)
    {
        if (Regex.Match(__0, "start_of_\\d.save$").Success)
        {
            var mission = (int) __instance.GameState.missionKey;
            var parts = __0.Split(Path.DirectorySeparatorChar);
            parts[parts.Length - 1] = $"{mission}_{parts[parts.Length - 1]}";
            __0 = String.Join(Path.DirectorySeparatorChar, parts);
        }
        return true;
    }
}
