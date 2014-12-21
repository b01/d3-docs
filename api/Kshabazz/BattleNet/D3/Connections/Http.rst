------------------------------------------
Kshabazz\\BattleNet\\D3\\Connections\\Http
------------------------------------------

.. php:namespace: Kshabazz\\BattleNet\\D3\\Connections

.. php:class:: Http

    Class Http

    .. php:const:: API_PROFILE_URL

    .. php:const:: API_HERO_URL

    .. php:const:: API_ITEM_URL

    .. php:const:: AUTHORIZE_URI

    .. php:const:: TOKEN_URI

    .. php:method:: __construct($pApiKey, $pBattleNetId, $pClient, $pLocale = 'en_US')

        Constructor

        :type $pApiKey: string
        :param $pApiKey:
        :type $pBattleNetId: string
        :param $pBattleNetId:
        :type $pClient: \Kshabazz\Slib\HttpClient
        :param $pClient:
        :type $pLocale: string
        :param $pLocale:

    .. php:method:: __destruct()

        Destructor

    .. php:method:: battleNetUrlSafeId()

        Get BattleNet ID

        :returns: string BattleNet ID

    .. php:method:: battleNetId()

        Get BattleNet ID

        :returns: string BattleNet ID

    .. php:method:: getHero($pHeroId)

        Request Hero JSON from Battle.Net.
        ex:
        https://us.api.battle.net/d3/profile/<battleNetIdName>-<battleNetIdNumber>/hero/<hero-id>?locale=<string>&apikey=<>
        Note: Leave off the trailing '/' when setting

        :param $pHeroId:
        :returns: null|string

    .. php:method:: getItem($pItemId)

        Get item JSON from Battle.Net D3 API.
        ex:
        https://us.battle.net/api/d3/data/item/COGHsoAIEgcIBBXIGEoRHYQRdRUdnWyzFB2qXu51MA04kwNAAFAKYJMD

        :param $pItemId:
        :returns: mixed|null

    .. php:method:: getItemsAsModels($pItemHashes)

        For each item the hero has equipped construct an Model\Item and return
        them as an array.
        This is costly, it make a HTTP request for each item on the hero.

        :type $pItemHashes: array
        :param $pItemHashes: List of item hashes.
        :returns: array|null

    .. php:method:: getProfile()

        ex:
        https://us.api.battle.net/d3/profile/<battleNetIdName>-<battleNetIdNumber>/

        :returns: null|string

    .. php:method:: setRegion($pRegion)

        Set the region.

        :param $pRegion:
        :returns: string

    .. php:method:: url()

        :returns: string

    .. php:method:: makeRequest($pUrl)

        Make a request to the currently set {@see $this->url}.

        :type $pUrl: string
        :param $pUrl:
        :returns: string|null
