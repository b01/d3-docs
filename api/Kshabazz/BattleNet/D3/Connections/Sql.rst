-----------------------------------------
Kshabazz\\BattleNet\\D3\\Connections\\Sql
-----------------------------------------

.. php:namespace: Kshabazz\\BattleNet\\D3\\Connections

.. php:class:: Sql

    Class Sql

    .. php:method:: __construct($pBattleNetId, PDO $pPdo, $pIpAddress = NULL)

        Constructor

        :type $pBattleNetId: string
        :param $pBattleNetId:
        :type $pPdo: PDO
        :param $pPdo:
        :type $pIpAddress: string
        :param $pIpAddress:

    .. php:method:: addRequest($pUrl)

        Add a record of the Battle.net Web API request.

        :type $pUrl: string
        :param $pUrl: The Battle.net url web API URL requested.
        :returns: bool|mixed

    .. php:method:: getHero($pHeroId)

        Get hero data from local database.

        :type $pHeroId: int
        :param $pHeroId:
        :returns: string|null

    .. php:method:: getItem($pItemHash)

        Get item JSON data from local database.

        :type $pItemHash: string
        :param $pItemHash:
        :returns: string|null

    .. php:method:: getItemsAsModels($pItemHashes)

        :param $pItemHashes:

    .. php:method:: getProfile()

        Get the profile from local database.

        :returns: string|null

    .. php:method:: saveHero($pHeroId, $pJson)

        Save the hero in a local database.

        :param $pHeroId:
        :param $pJson:
        :returns: bool Indicates success (TRUE) or failure (FALSE).

    .. php:method:: saveItem(Item $pItem, $shaString)

        Save the item locally in a database.

        :type $pItem: Item
        :param $pItem:
        :type $shaString: string
        :param $shaString: A unique string to use as a SHA seed for the item SHA value in the database.
        :returns: bool

    .. php:method:: saveProfile($pJson)

        Save the users profile locally to the database.

        :type $pJson: string
        :param $pJson:
        :returns: bool
