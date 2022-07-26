# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = apifox_modal_from_dict(json.loads(json_string))

from suds.client import Client  # 导入suds.client 模块下的Client类


def from_str(x):
    assert isinstance(x, str)
    return x


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class MsgHeader:
    def __init__(self, batch_no, current_count, current_page, partner_name, partner_type, sellout_type, submit_date, token, total_count, total_page):
        self.batch_no = batch_no
        self.current_count = current_count
        self.current_page = current_page
        self.partner_name = partner_name
        self.partner_type = partner_type
        self.sellout_type = sellout_type
        self.submit_date = submit_date
        self.token = token
        self.total_count = total_count
        self.total_page = total_page

    @staticmethod
    def from_dict(obj):
        batch_no = from_str(obj.get("BATCH_NO"))
        current_count = from_str(obj.get("CURRENT_COUNT"))
        current_page = from_str(obj.get("CURRENT_PAGE"))
        partner_name = from_str(obj.get("PARTNER_NAME"))
        partner_type = from_str(obj.get("PARTNER_TYPE"))
        sellout_type = from_str(obj.get("SELLOUT_TYPE"))
        submit_date = from_str(obj.get("SUBMIT_DATE"))
        token = from_str(obj.get("TOKEN"))
        total_count = from_str(obj.get("TOTAL_COUNT"))
        total_page = from_str(obj.get("TOTAL_PAGE"))
        return MsgHeader(batch_no, current_count, current_page, partner_name, partner_type, sellout_type, submit_date, token, total_count, total_page)

    def to_dict(self):
        result = {}
        result["BATCH_NO"] = from_str(self.batch_no)
        result["CURRENT_COUNT"] = from_str(self.current_count)
        result["CURRENT_PAGE"] = from_str(self.current_page)
        result["PARTNER_NAME"] = from_str(self.partner_name)
        result["PARTNER_TYPE"] = from_str(self.partner_type)
        result["SELLOUT_TYPE"] = from_str(self.sellout_type)
        result["SUBMIT_DATE"] = from_str(self.submit_date)
        result["TOKEN"] = from_str(self.token)
        result["TOTAL_COUNT"] = from_str(self.total_count)
        result["TOTAL_PAGE"] = from_str(self.total_page)
        return result


class MsgLine:
    def __init__(self, date, ecommerce_platform_name, ecommerce_store_type, final_cust_id, industry, product_sn, return_reason, ship_from_province, ship_to_address):
        self.date = date
        self.ecommerce_platform_name = ecommerce_platform_name
        self.ecommerce_store_type = ecommerce_store_type
        self.final_cust_id = final_cust_id
        self.industry = industry
        self.product_sn = product_sn
        self.return_reason = return_reason
        self.ship_from_province = ship_from_province
        self.ship_to_address = ship_to_address

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        date = from_str(obj.get("DATE"))
        ecommerce_platform_name = from_str(obj.get("ECOMMERCE_PLATFORM_NAME"))
        ecommerce_store_type = from_str(obj.get("ECOMMERCE_STORE_TYPE"))
        final_cust_id = from_str(obj.get("FINAL_CUST_ID"))
        industry = from_str(obj.get("INDUSTRY"))
        product_sn = from_str(obj.get("PRODUCT_SN"))
        return_reason = from_str(obj.get("RETURN_REASON"))
        ship_from_province = from_str(obj.get("SHIP_FROM_PROVINCE"))
        ship_to_address = from_str(obj.get("SHIP_TO_ADDRESS"))
        return MsgLine(date, ecommerce_platform_name, ecommerce_store_type, final_cust_id, industry, product_sn, return_reason, ship_from_province, ship_to_address)

    def to_dict(self):
        result = {}
        result["DATE"] = from_str(self.date)
        result["ECOMMERCE_PLATFORM_NAME"] = from_str(self.ecommerce_platform_name)
        result["ECOMMERCE_STORE_TYPE"] = from_str(self.ecommerce_store_type)
        result["FINAL_CUST_ID"] = from_str(self.final_cust_id)
        result["INDUSTRY"] = from_str(self.industry)
        result["PRODUCT_SN"] = from_str(self.product_sn)
        result["RETURN_REASON"] = from_str(self.return_reason)
        result["SHIP_FROM_PROVINCE"] = from_str(self.ship_from_province)
        result["SHIP_TO_ADDRESS"] = from_str(self.ship_to_address)
        return result


class MsgLines:
    def __init__(self, msg_line):
        self.msg_line = msg_line

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        msg_line = MsgLine.from_dict(obj.get("MsgLine"))
        return MsgLines(msg_line)

    def to_dict(self):
        result = {}
        result["MsgLine"] = to_class(MsgLine, self.msg_line)
        return result


class GolGoldenSellOut:
    def __init__(self, msg_header, msg_lines):
        self.msg_header = msg_header
        self.msg_lines = msg_lines

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        msg_header = MsgHeader.from_dict(obj.get("MsgHeader"))
        msg_lines = MsgLines.from_dict(obj.get("MsgLines"))
        return GolGoldenSellOut(msg_header, msg_lines)

    def to_dict(self):
        result = {}
        result["MsgHeader"] = to_class(MsgHeader, self.msg_header)
        result["MsgLines"] = to_class(MsgLines, self.msg_lines)
        return result


class SoapenvBody:
    def __init__(self, gol_golden_sell_out):
        self.gol_golden_sell_out = gol_golden_sell_out

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        gol_golden_sell_out = GolGoldenSellOut.from_dict(obj.get("gol:GoldenSellOut"))
        return SoapenvBody(gol_golden_sell_out)

    def to_dict(self):
        result = {}
        result["gol:GoldenSellOut"] = to_class(GolGoldenSellOut, self.gol_golden_sell_out)
        return result


class From:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        return From(name)

    def to_dict(self):
        result = {}
        result["name"] = from_str(self.name)
        return result


class To:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        return To(name)

    def to_dict(self):
        result = {}
        result["name"] = from_str(self.name)
        return result


class ParPartyInfo:
    def __init__(self, par_party_info_from, operation_id, operation_type, to, transaction_id):
        self.par_party_info_from = par_party_info_from
        self.operation_id = operation_id
        self.operation_type = operation_type
        self.to = to
        self.transaction_id = transaction_id

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        par_party_info_from = From.from_dict(obj.get("from"))
        operation_id = from_str(obj.get("operationID"))
        operation_type = from_str(obj.get("operationType"))
        to = To.from_dict(obj.get("to"))
        transaction_id = from_str(obj.get("transactionID"))
        return ParPartyInfo(par_party_info_from, operation_id, operation_type, to, transaction_id)

    def to_dict(self):
        result = {}
        result["from"] = to_class(From, self.par_party_info_from)
        result["operationID"] = from_str(self.operation_id)
        result["operationType"] = from_str(self.operation_type)
        result["to"] = to_class(To, self.to)
        result["transactionID"] = from_str(self.transaction_id)
        return result


class SoapenvHeader:
    def __init__(self, par_party_info):
        self.par_party_info = par_party_info

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        par_party_info = ParPartyInfo.from_dict(obj.get("par:PartyInfo"))
        return SoapenvHeader(par_party_info)

    def to_dict(self):
        result = {}
        result["par:PartyInfo"] = to_class(ParPartyInfo, self.par_party_info)
        return result


class ApifoxModal:
    def __init__(self, soapenv_body, soapenv_header):
        self.soapenv_body = soapenv_body
        self.soapenv_header = soapenv_header

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        soapenv_body = SoapenvBody.from_dict(obj.get("soapenv:Body"))
        soapenv_header = SoapenvHeader.from_dict(obj.get("soapenv:Header"))
        return ApifoxModal(soapenv_body, soapenv_header)

    def to_dict(self):
        result = {}
        result["soapenv:Body"] = to_class(SoapenvBody, self.soapenv_body)
        result["soapenv:Header"] = to_class(SoapenvHeader, self.soapenv_header)
        return result


def apifox_modal_from_dict(s):
    return ApifoxModal.from_dict(s)


def apifox_modal_to_dict(x):
    return to_class(ApifoxModal, x)



if __name__ == '__main__':
        t=Client('https://apigw-beta.huawei.com/api/SOAP?X-HW-APPKEY=cVboSZsFApMMJ5vvUCd9PA==&X-HW-ID=com.huawei.b2b.b2bextcust')
        t.service.SO()
        req = str(t.last_sent())  # 保存请求报文，因为返回的是一个实例，所以要转换成str
        response = str(t.last_received())  # 保存返回报文，返回的也是一个实例
        print(req)  # 打印请求报文
        print('***************--下面是返回的报文******************')
        print(response)  # 打印返回报文


