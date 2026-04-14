using Data;
using HarmonyLib;
using Model;
using Model.State;
using System.Collections.Generic;
using System.Reflection;

namespace TerraNilAP;

[HarmonyPatch(typeof(GameState), "ExecuteCommand")]
class GameStateSyncPatch
{
    public static void Postfix(GameState __instance)
    {
        var logic = TerraNilAP.MissionLogic.GetValueSafe(__instance.missionKey);
        if (logic != null)
        {
            logic.Update(__instance);
        }
    }
}
