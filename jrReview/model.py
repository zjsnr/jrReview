import datetime


class Ship:
    def __init__(self, data: dict):
        def f(key, type=int):
            return type(data[key])
        self.id = f('id')
        self.name = f('title', str)
        self.cid = f('shipCid')
        self.type = f('type')
        self.level = f('level')
        self.birthday = datetime.datetime.fromtimestamp(f('create_time'))
        # 出征相关
        self.sinkNum = f('sink_num')  # 沉船次数
        self.skinCid = f('skin_cid')
        self.pveTotal = f('fight_num')  # 出征次数
        self.hurtShipNum = f('hurt_ship_num')  # 造成的总伤害
        self.sinkShipNum = f('sink_ship_num')  # 击沉的船的数量
        self.missNum = f('miss_num')  # 闪避攻击的次数
        self.pvpWinNum = f('pvp_win_num')  # 演习胜利次数
        self.repairNum = f('repair_num')  # 修理次数
        self.medals = data['active_medal']  # 奖章列表
        self.medalNum = len(self.medals)
        self.tactics = [int(_) for _ in data['tactics']]
        # self.tacticNum = len(self.tactics)
        # 消耗
        self.ammoCost = f('ammo_num')  # 弹药消耗
        self.steelCost = f('steel_num')  # 钢
        self.oilCost = f('oil_num')
        self.alCost = f('aluminium_num')
        # 结婚好感
        self.married = f('married', bool)
        if self.married:
            self.marriedTime = datetime.datetime.fromtimestamp(f('marry_time'))
        else:
            self.marriedTime = None
        self.love = f('love')
        self.loveMax = f('loveMax')
        # 其他
        self.buildBoatNum = f('build_boat_num')

    def __repr__(self):
        return f'<Ship {self.name} lv.{self.level}>'


class Tactic:
    def __init__(self, data: dict):
        def f(key, type=int):
            return type(data[key])
        self.shipId = f('boat_id')
        self.level = f('level')
        self.exp = f('exp')
        self.tacticId = f('tactics_id')


class User:
    def __init__(self, data):
        self.level = int(data['userVo']['level'])
        detailInfo = data['userVo']['detailInfo']
        self.pveTotal = int(detailInfo['pveNum'])
        self.pveWin = int(detailInfo['pveWin'])
        self.pvpTotal = int(detailInfo['pvpNum'])
        self.pvpWin = int(detailInfo['pvpWin'])
        self.collectionPercentage = detailInfo['collection']
        self.shipNumMax = int(data['userVo']['shipNumTop'])

        self.equipTotal = sum(int(item['num']) for item in data['equipmentVo'])

        self.ships = [Ship(item) for item in data['userShipVO']]

        self.tactics = [Tactic(item) for item in data['tactics']]
