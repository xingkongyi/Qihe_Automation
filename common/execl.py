from openpyxl import load_workbook


def read_excel(file, sheet_name):
    """读取excel数据"""
    # 得到 wb
    wb = load_workbook(file)
    # 得到 sheet,  wb["Sheet1"]
    sheet = wb[sheet_name]
    # 得到所有的数据
    data_list = list(sheet.values)
    # 获取所有的标题
    titles = data_list[0]
    # 转化成字典
    rows = [dict(zip(titles, row)) for row in data_list[1:]]
    return rows


if __name__ == '__main__':
    execl_path = r'D:\Python\Qihe_Automation\data\qihe_case.xlsx'
    data = read_excel(execl_path, 'event_acceptance_query')
    print(data)
