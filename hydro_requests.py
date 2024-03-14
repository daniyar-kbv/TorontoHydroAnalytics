import datetime as dt
import requests

cookies = {
    '_ga_HBH4QCXK8M': 'GS1.1.1710378506.1.1.1710384623.18.0.0',
    '_ga': 'GA1.2.1288185570.1710378506',
    '_ga_X51C15411B': 'GS1.2.1710378606.1.1.1710384620.0.0.0',
    '_gat_UA-2692436-1': '1',
    '_gid': 'GA1.2.1734573508.1710378507',
    'LFR_SESSION_STATE_188279107': '1710384590961',
    '_gat': '1',
    'LFR_SESSION_STATE_20120': '1710383063360',
    'dtPC': '1$381039416_630h-vMOFPMJSRMQSBMWLROPARPPQGIBFNJALT-0e0',
    'dtCookie': 'v_4_srv_1_sn_DA865148988ADE5B243C4821FD44F1A0_perc_100000_ol_0_mul_1_app-3Aef70a32d994c2692_1',
    'dtSa': 'true%7CKD%7C-1%7CPage%3A%20my-usage%3Fp_p_id%3Dth_module_custom_sessiontimeout_ThModuleCustomSessiontimeoutPortlet_INSTANC...%7C-%7C1710381553410%7C381039416_630%7Chttps%3A%2F%2Fwww.torontohydro.com%2Fmy-account%2Fmy-usage%3Fp_5Fp_5Fid%3Dth_5Fmodule_5Fcustom_5Fsessiontimeout_5FThModuleCustomSessiontimeoutPortlet_5FINSTANCE_5FthcGlobalModuleCustomSessiontimeoutPortlet%26p_5Fp_5Flifecycle%3D1%26p_5Fp_5Fstate%3Dnormal%26p_5Fp_5Fmode%3Dview%26_5Fth_5Fmodule_5Fcustom_5Fsessiontimeout_5FThModuleCustomSessiontimeoutPortlet_5FINSTANCE_5FthcGlobalModuleCustomSessiontimeoutPortlet_5Fjavax.portlet.action%3D_252Flogout%26_5Fth_5Fmodule_5Fcustom_5Fsessiontimeout_5FThModuleCustomSessiontimeoutPortlet_5FINSTANCE_5FthcGlobalModuleCustomSessiontimeoutPortlet_5FsessionExpired%3Dtrue%26p_5Fauth%3DqUqQz5PE%7C%7C%7C%7C',
    'rxVisitor': '1710380972264Q74RE9SFQQARBETHF62V5SI71F4KP1DC',
    'rxvt': '1710382841705|1710380972264',
    'incap_ses_1444_2468062': 's4vpFXQFOhGkdNJcLR8KFKtX8mUAAAAAyZveGTMQn4ubF3MvhMwQDw==',
    'nmstat': 'c30bff22-1eae-7f06-e66d-59aae3abb734',
    'incap_ses_303_2468062': 'tuP0HpBwkD2lUmJp53g0BAlO8mUAAAAA747/Zmsz8RjeSOUq6jRCdw==',
    'visid_incap_2468062': 'WbGXJKCIRpqYBSp0hstecBY6VGUAAAAAQUIPAAAAAADtbRrYbW5h7dRp62gfWSPu',
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'en-CA,en-US;q=0.9,en;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'cors',
    'Host': 'www.torontohydro.com',
    'Origin': 'https://www.torontohydro.com',
    # 'Content-Length': '50',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15',
    'Referer': 'https://www.torontohydro.com/my-account/my-usage?p_p_id=th_module_custom_sessiontimeout_ThModuleCustomSessiontimeoutPortlet_INSTANCE_thcGlobalModuleCustomSessiontimeoutPortlet&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&_th_module_custom_sessiontimeout_ThModuleCustomSessiontimeoutPortlet_INSTANCE_thcGlobalModuleCustomSessiontimeoutPortlet_javax.portlet.action=%2Flogout&_th_module_custom_sessiontimeout_ThModuleCustomSessiontimeoutPortlet_INSTANCE_thcGlobalModuleCustomSessiontimeoutPortlet_sessionExpired=true&p_auth=qUqQz5PE',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    # 'Cookie': '_ga_HBH4QCXK8M=GS1.1.1710378506.1.1.1710384623.18.0.0; _ga=GA1.2.1288185570.1710378506; _ga_X51C15411B=GS1.2.1710378606.1.1.1710384620.0.0.0; _gat_UA-2692436-1=1; _gid=GA1.2.1734573508.1710378507; LFR_SESSION_STATE_188279107=1710384590961; _gat=1; JSESSIONID=0000MhxMZM2wSEznorxRNB3SVt6:1gupvju42; LFR_SESSION_STATE_20120=1710383063360; dtPC=1$381039416_630h-vMOFPMJSRMQSBMWLROPARPPQGIBFNJALT-0e0; dtCookie=v_4_srv_1_sn_DA865148988ADE5B243C4821FD44F1A0_perc_100000_ol_0_mul_1_app-3Aef70a32d994c2692_1; dtSa=true%7CKD%7C-1%7CPage%3A%20my-usage%3Fp_p_id%3Dth_module_custom_sessiontimeout_ThModuleCustomSessiontimeoutPortlet_INSTANC...%7C-%7C1710381553410%7C381039416_630%7Chttps%3A%2F%2Fwww.torontohydro.com%2Fmy-account%2Fmy-usage%3Fp_5Fp_5Fid%3Dth_5Fmodule_5Fcustom_5Fsessiontimeout_5FThModuleCustomSessiontimeoutPortlet_5FINSTANCE_5FthcGlobalModuleCustomSessiontimeoutPortlet%26p_5Fp_5Flifecycle%3D1%26p_5Fp_5Fstate%3Dnormal%26p_5Fp_5Fmode%3Dview%26_5Fth_5Fmodule_5Fcustom_5Fsessiontimeout_5FThModuleCustomSessiontimeoutPortlet_5FINSTANCE_5FthcGlobalModuleCustomSessiontimeoutPortlet_5Fjavax.portlet.action%3D_252Flogout%26_5Fth_5Fmodule_5Fcustom_5Fsessiontimeout_5FThModuleCustomSessiontimeoutPortlet_5FINSTANCE_5FthcGlobalModuleCustomSessiontimeoutPortlet_5FsessionExpired%3Dtrue%26p_5Fauth%3DqUqQz5PE%7C%7C%7C%7C; rxVisitor=1710380972264Q74RE9SFQQARBETHF62V5SI71F4KP1DC; rxvt=1710382841705|1710380972264; incap_ses_1444_2468062=s4vpFXQFOhGkdNJcLR8KFKtX8mUAAAAAyZveGTMQn4ubF3MvhMwQDw==; nmstat=c30bff22-1eae-7f06-e66d-59aae3abb734; incap_ses_303_2468062=tuP0HpBwkD2lUmJp53g0BAlO8mUAAAAA747/Zmsz8RjeSOUq6jRCdw==; visid_incap_2468062=WbGXJKCIRpqYBSp0hstecBY6VGUAAAAAQUIPAAAAAADtbRrYbW5h7dRp62gfWSPu',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'p_p_id': 'thmoduletou',
    'p_p_lifecycle': '2',
    'p_p_state': 'normal',
    'p_p_mode': 'view',
    'p_p_resource_id': 'getHourlyChartData',
    'p_p_cacheability': 'cacheLevelPage',
}

data = {
    'spIDs': '0046201097',
    'meterNum': '70090562',
}

def request_hourly(jsession_id, date):
    cookies['JSESSIONID'] = jsession_id
    data['date'] = date

    print('Requesting hourly data for ' + date)
    response = requests.post(
        'https://www.torontohydro.com/my-account/my-usage',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print('Response received, status code: ' + str(response.status_code))
    return response