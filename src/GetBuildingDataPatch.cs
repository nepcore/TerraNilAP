using Data;
using HarmonyLib;
using Model;
using Model.Buildings;

namespace TerraNilAP;

[HarmonyPatch(typeof(BuildingFactory), "GetBuildingDataForType")]
class GetBuldingDataPatch
{
    public static void Postfix(object[] __args, ref BuildingData __result)
    {
        var type = (Type) __args[0];
        __result.showCondition = new APUnlockCondition(type);
        __result.unlockCondition = new APUnlockCondition(type);
    }
}
