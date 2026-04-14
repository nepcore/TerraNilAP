using Data.BuildingButtonUnlockConditions;
using Global;
using Model;
using System.Linq;
using Utils;

namespace TerraNilAP;

class APUnlockCondition : BuildingButtonUnlockCondition
{
    public APUnlockCondition(Type type)
    {
        this.type = type;
        this.ignoreReUnlockConditionFor = new Mission[0];
    }

    private int ItemsReceived()
    {
        var mission = (uint) MonoSingleton<CampaignStateManager>.Instance.GameState.missionKey;
        var building = (uint) this.type;
        var id = (1u << 31) | (1u << 30) | (mission << 12) | building;
        return TerraNilAP.Session.Items.AllItemsReceived.Select(item => item.ItemId).Contains(id) ? 1 : 0;
    }

    public override float GetProgress()
    {
        return ItemsReceived();
    }

    public override float GetProgress(Model.State.GameState state)
    {
        return ItemsReceived();
    }

    public override int GetProgressRemaining()
    {
        return 1 - ItemsReceived();
    }

    public override int GetProgressRequired()
    {
        return 1;
    }

    public override string GetUnlockHoverText()
    {
        return "Unlocked by Archipelago";
    }

    public override UnityEngine.Sprite GetIconForCondition()
    {
        return TerraNilAP.SpriteFromResource("TerraNilAP.assets.archipelago.png");
    }
}
