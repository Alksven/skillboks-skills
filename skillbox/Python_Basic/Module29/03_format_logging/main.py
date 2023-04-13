import datetime


def log_methods(form_data):
    def wrapper_method(method):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            print(f"Запускается '{method.__qualname__}'. Дата и время запуска: {start_time.strftime(form_data)}.")
            result = method(*args, **kwargs)
            stop_time = datetime.datetime.now()
            run_time = stop_time - start_time
            print(f"Завершение '{method.__qualname__}', время работы = {run_time} s. ")
            return result
        return wrapper

    def class_wrapper(cls):
        for name, method in cls.__dict__.items():
            if callable(method) and not name.startswith("__"):
                setattr(cls, name, wrapper_method(method))
        return cls
    return class_wrapper


@log_methods("%B %d %Y - %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')

        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(1000)])

        return result


@log_methods("%B %d %Y - %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")

        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(1000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()