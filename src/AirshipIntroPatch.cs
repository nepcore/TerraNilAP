using HarmonyLib;
using View.Handlers;

namespace TerraNilAP;

[HarmonyPatch(typeof(AirshipDecontructIntroHandler), "LateStart")]
class AirshipIntroPatch
{
    public static bool Prefix()
    {
        return false;
    }
}
