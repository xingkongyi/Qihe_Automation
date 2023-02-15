from faker import Faker


def generate_mobile():
    """生成手机号码"""
    faker = Faker(locale=['zh-cn'])
    print(faker.phone_number())
    # 生成手机号码
    return faker.phone_number()


def generate_idcard():
    """生成身份证"""
    faker = Faker(locale=['zh-cn'])
    print(faker.ssn())
    # 生成身份证
    return faker.ssn()

generate_mobile()
generate_idcard()
