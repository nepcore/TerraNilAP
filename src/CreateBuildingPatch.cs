using HarmonyLib;
using Model;
using Model.Buildings;

namespace TerraNilAP;

[HarmonyPatch(typeof(BuildingFactory), "CreateBuilding", new System.Type[4] {typeof(Type), typeof(int), typeof(int), typeof(int)})]
class CreateBuildingPatch
{
    public static void Postfix(object[] __args, Building __result)
    {
        var type = (Type) __args[0];
        __result.BuildingData.showCondition = new APUnlockCondition(type);
        __result.BuildingData.unlockCondition = new APUnlockCondition(type);
    }
}
