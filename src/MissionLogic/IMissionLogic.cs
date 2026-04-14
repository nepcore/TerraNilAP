using Model;
using Model.State;

namespace TerraNilAP.MissionLogic;

public interface IMissionLogic
{
    public Mission Target();
    public void Update(GameState state);
}

public static class MissionLogicExtensions
{
    public static long Location<T>(this T logic, uint id) where T : IMissionLogic
    {
        var mission = (uint)logic.Target();
        return (1u << 31) | (mission << 12) | id;
    }
}
