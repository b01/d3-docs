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
        :param $pApiKey: Key obtained for use with Diablo 3 REST service.
        :type $pBattleNetId: string
        :param $pBattleNetId: BattleNet ID.
        :type $pClient: \Kshabazz\Slib\HttpClient
        :param $pClient: Client for making HTTP request.
        :type $pLocale: string
        :param $pLocale:

    .. php:method:: __destruct()

        Destructor

    .. php:method:: battleNetUrlSafeId()

        Get BattleNet ID with the pound symbol replaced with a dash.

        :returns: string BattleNet ID

    .. php:method:: battleNetId()

        Get BattleNet ID

        :returns: string BattleNet ID

    .. php:method:: getHero($pHeroId)

        Request Hero JSON from Battle.Net.

        <code>
        <?php
        // Make a request to:
        //
        https://us.api.battle.net/d3/profile/<battleNetIdName>-<battleNetIdNumber>/hero/<hero-id>?locale=<string>&apikey=<>
        // Note: Leave off the trailing '/' when setting
        ?>
        </code>

        :type $pHeroId: int
        :param $pHeroId: Hero ID.
        :returns: null|string

    .. php:method:: getItem($pItemId)

        Make a request to the API to get an item (JSON).

        <code>
        // Make a request to:
        //
        https://us.battle.net/api/d3/data/item/COGHsoAIEgcIBBXIGEoRHYQRdRUdnWyzFB2qXu51MA04kwNAAFAKYJMD
        </code>

        :type $pItemId: string
        :param $pItemId: Can be obtained from items a hero has equipped.
        :returns: string|null API JSON data.

    .. php:method:: getItemsAsModels($pItemHashes)

        For each item the hero has equipped construct an Model\Item and return
        them as an array.
        This is costly, it makes an HTTP request for each item in the list.

        :type $pItemHashes: array
        :param $pItemHashes: List of item hash IDs.
        :returns: array|null Item models

    .. php:method:: getProfile()

        Get a profile from Battle.net.
        <code>
        // Makes a request to:
        https://us.api.battle.net/d3/profile/<battleNetIdName>-<battleNetIdNumber>/

        </code>

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
