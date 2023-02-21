from shop import user_interface


def run_homework():
    if user_interface.load_stock():
        user_interface.handle_customer()
        user_interface.save_stock()


if __name__ == '__main__':
    run_homework()
