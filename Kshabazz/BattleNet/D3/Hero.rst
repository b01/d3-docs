-----------------------------
Kshabazz\\BattleNet\\D3\\Hero
-----------------------------

.. php:namespace: Kshabazz\\BattleNet\\D3

.. php:class:: Hero

    Class Hero

    .. php:method:: __construct($pJson)

        Constructor

        :type $pJson: string
        :param $pJson:

    .. php:method:: arcaneResist()

        Get arcane resist.

        :returns: int

    .. php:method:: armor()

        Get armor stat.

        :returns: int

    .. php:method:: attackSpeed()

        Get attack speed.

        :returns: float

    .. php:method:: characterClass()

        Character class

        :returns: string (barbarian|crusader|demon-hunter|monk|witch-doctor|wizard)

    .. php:method:: coldResist()

        Get cold resist.

        :returns: int

    .. php:method:: criticalHitChance()

        :returns: float

    .. php:method:: criticalHitDamage()

        :returns: float

    .. php:method:: dexterity()

        Get dexterity.

        :returns: int

    .. php:method:: eliteKills()

        Get number of elites killed.

        :returns: int

    .. php:method:: fireResist()

        Get fire resist.

        :returns: int

    .. php:method:: gender()

        Get gender.

        :returns: int 0 for male, 1 for woman.

    .. php:method:: get($pProperty, $pType = 'string')

        Get data from the hero JSON data retrieved from Battle.net API.

        :type $pProperty: string
        :param $pProperty:
        :type $pType: string
        :param $pType:
        :returns: mixed

    .. php:method:: highestProgression()

        Get the highest level completed.

        :returns: string

    .. php:method:: id()

        :returns: int

    .. php:method:: intelligence()

        Get intelligence.

        :returns: int

    .. php:method:: isDead()

        Indicates whether the Hero has fallen.

        :returns: bool

    .. php:method:: isDualWielding(Http $pHttp)

        Determine if a hero is brandishing a weapon in each hand.

        :type $pHttp: Http
        :param $pHttp:
        :returns: bool

    .. php:method:: isHardCore()

        Get hardcore flag.

        :returns: bool

    .. php:method:: isSeasonal()

        Get seasonal flag.

        :returns: bool

    .. php:method:: items()

        Get items.

        :returns: array

    .. php:method:: itemsHashesBySlot()

        Get a list of hashes for each item the hero has equipped.

        :returns: array|null Null when the hero has no items equipped.

    .. php:method:: json()

        Get JSON.

        :returns: string JSON passed into constructor.

    .. php:method:: lastUpdated()

        Get when last updated.

        :returns: string

    .. php:method:: level()

        Get level.

        :returns: int

    .. php:method:: lightningResist()

        Get lightning resistance.

        :returns: int

    .. php:method:: name()

        Get name.

        :returns: string

    .. php:method:: paragonLevel()

        Get paragon level.

        :returns: int

    .. php:method:: physicalResist()

        Get physical resistance.

        :returns: int

    .. php:method:: poisonResist()

        Get poison resistance.

        :returns: int

    .. php:method:: preCalculatedStats()

        Get character stats calculated by Battle.Net.

        :returns: array

    .. php:method:: primaryAttribute()

        Get primary attribute.

        :returns: string

    .. php:method:: progression()

        Get hero act progress.

        :returns: array

    .. php:method:: punchDamage()

        Get damage you can do with a single punch.

        :returns: float

    .. php:method:: skills()

        Get character skills.

        :returns: array

    .. php:method:: primaryAttributeBonus()

        Get primary stat bonus (bonuses from items not included).

        :returns: int

    .. php:method:: strength()

        Get strength.

        :returns: int

    .. php:method:: vitality()

        Get vitality.

        :returns: int

    .. php:method:: baseAttributeLevelBonus($pProperty, $pMultiplier)

        Black box for computing the total for
        dexterity/intelligence/strength/vitality.

        :type $pProperty: string
        :param $pProperty:
        :type $pMultiplier: int
        :param $pMultiplier:

    .. php:method:: determinePrimaryAttribute()

        Use the hero's class to determine the primary attribute.

        :returns: string

    .. php:method:: init()

        :returns: $this
