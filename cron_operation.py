from cron_field import CronField, Minute


class CronExpOperation:
    @classmethod
    def asterisk_operation(cls, field_type: CronField):
        start, end = field_type.get_limits()
        values = [i for i in range(start, end + 1)]
        field_instance = field_type(values)

        return field_instance

    @classmethod
    def range_step_operation(cls, cron_field_exp: str, field_type: CronField):
        start_num, step_size = cron_field_exp.split("/")
        start, end = field_type.get_limits()

        params = []
        if start_num != "*":
            params.append(start_num)
        params.append(step_size)
        params = field_type.parse(params)
        step_size = params[-1]

        if start_num != "*":
            start_num = params[0]
            start = start_num
        elif start % step_size != 0:
            start = step_size

        values = [i for i in range(start, end + 1, step_size)]
        field_instance = field_type(values)
        if not field_instance.validate():
            raise Exception(f"Error while validating {field_instance.__class__.__name__} data {values}")

        return field_instance

    @classmethod
    def range_operation(cls, cron_field_exp: str, field_type: CronField):
        start_num, end_num = cron_field_exp.split("-")
        params = field_type.parse([start_num, end_num])
        start = params[0]
        end = params[1]

        values = [i for i in range(start, end + 1)]
        field_instance = field_type(values)
        if not field_instance.validate():
            raise Exception(f"Error while validating {field_instance.__class__.__name__} data {values}")
        # field_instance.validate()

        return field_instance

    @classmethod
    def comma_operation(cls, cron_field_exp: str, field_type: CronField):
        values = cron_field_exp.split(",")
        values = field_type.parse(values)

        field_instance = field_type(values)
        if not field_instance.validate():
            raise Exception(f"Error while validating {field_instance.__class__.__name__} data {values}")
        # field_instance.validate()

        return field_instance

    @classmethod
    def single_value_operation(cls, cron_field_exp: str, field_type: CronField):
        values = field_type.parse([cron_field_exp])

        field_instance = field_type(values)
        if not field_instance.validate():
            raise Exception(f"Error while validating {field_instance.__class__.__name__} data {values}")
        # field_instance.validate()

        return field_instance
