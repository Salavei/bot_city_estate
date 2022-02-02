import sqlite3


class SQLestate:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    # SQL ANNOUNCEMENTS ONLY

    def add_announcements_rent(self, price, number_of_rooms, street, rent_description, phone, photo,
                               date_time, tg_id, placed, allow=True, allow_admin=False):
        """Добавляем обьявление аренды"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `announcements_rent` (`price`,`number_of_rooms`,`street`,"
                "`rent_description`,`phone`,`placed`, `photo`, `date_time`, `allow_admin`, `allow`, `tg_id`) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                (price, number_of_rooms, street, rent_description, phone, placed, photo,
                 date_time, allow, allow_admin, tg_id))

    def add_announcements_sell(self, price, number_of_rooms, street, rent_description, phone, photo,
                               date_time, tg_id, placed, allow=True, allow_admin=False):
        """Добавляем обьявление продажи"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `announcements_sell` (`price`,`number_of_rooms`,`street`,"
                "`rent_description`,`phone`,`placed`, `photo`, `date_time`, `allow_admin`, `allow`, `tg_id`) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                (price, number_of_rooms, street, rent_description, phone, placed, photo,
                 date_time, allow, allow_admin, tg_id))

    def add_request_rent(self, id_an_rent, number_request, name_request):
        """Добавляем запрос аренды"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `request_rent` (`id_an_rent`,`number_request`,`name_request`) VALUES(?,?,?)",
                (id_an_rent, number_request, name_request))

    def add_request_sell(self, id_an_sell, number_request, name_request):
        """Добавляем запрос продажи"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `request_sell` (`id_an_sell`,`number_request`,`name_request`) VALUES(?,?,?)",
                (id_an_sell, number_request, name_request))

    def show_request_sell(self, id_an_rent):
        """показывает запрос продажи"""
        with self.connection:
            return self.cursor.execute(
                "SELECT `number_request`, `name_request`,`id_an_sell` FROM `request_sell` WHERE `id_an_sell` IN (SELECT `id` FROM `announcements_sell` WHERE `tg_id` =? )",
                (int(id_an_rent),)).fetchall()

    def show_request_rent(self, id_an_rent):
        """показывает запрос аренды"""
        with self.connection:
            return self.cursor.execute(
                "SELECT `number_request`, `name_request`,`id_an_rent` FROM `request_rent` WHERE `id_an_rent` IN (SELECT `id` FROM `announcements_rent` WHERE `tg_id` =? )",
                (int(id_an_rent),)).fetchall()

    def show_all_announcements_sell(self, ):
        """Показать все объявления по продаже"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_sell` WHERE `allow_admin` = ? and `allow` = ?",
                                       (True, True,)).fetchall()

    def show_all_announcements_rent(self, ):
        """Показать все объявления по аренде"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_rent` WHERE `allow_admin` = ? and `allow` = ?",
                                       (True, True,)).fetchall()

    def show_all_my_announcements_rent(self, tg_id):
        """Показать все объявления по аренде"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_rent` WHERE `tg_id` = ?", (tg_id,)).fetchall()

    def show_all_my_announcements_rent_request(self, id_an):
        """Показать все объявления по аренде для запросов"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_rent` WHERE `id` = ?", (id_an,)).fetchall()

    def show_all_my_announcements_sell(self, tg_id):
        """Показать все объявления по продаже"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_sell` WHERE `tg_id` = ?", (tg_id,)).fetchall()

    def show_all_my_announcements_sell_request(self, id_an):
        """Показать все объявления по продаже для запросов"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_sell` WHERE `id` = ?", (id_an,)).fetchall()


    # SQL USERS ONLY

    def check_subscriber(self, tg_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `tg_id` = ?', (tg_id,)).fetchall()
            return bool(len(result))

    def subscriber_exists(self):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users`', ).fetchall()
            return len(result)

    def start_my_announcements_rent(self, id):
        """Проверяем, на запуск аренды"""
        with self.connection:
            return self.cursor.execute('SELECT `allow` FROM `announcements_rent` WHERE `id` = ?', (id,)).fetchone()[0]

    def start_my_announcements_sell(self, id):
        """Проверяем, на запуск продажи"""
        with self.connection:
            return self.cursor.execute('SELECT `allow` FROM `announcements_sell` WHERE `id` = ?', (id,)).fetchone()[0]

    def add_subscriber(self, tg_id, admin=False):
        """Добавляем нового юзера"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`id`,`tg_id`, `admin`) VALUES(?,?,?)",
                                       (int(self.subscriber_exists()) + 1, tg_id, admin))

    def confirm_announcements_sell_user(self, id_conf, allow):
        """Подтвердить объявление продажи как юзер"""
        with self.connection:
            return self.cursor.execute("UPDATE `announcements_sell` SET `allow_admin` = ?, `allow` = ? WHERE `id` =?",
                                       (True, allow, id_conf))

    def confirm_announcements_rent_user(self, id_conf, allow):
        """Подтвердить объявление arend как юзер"""
        with self.connection:
            return self.cursor.execute("UPDATE `announcements_rent` SET `allow_admin` = ?, `allow` = ? WHERE `id` =?",
                                       (True, allow, id_conf))

    def confirm_announcements_sell_admin(self, id_conf):
        """Подтвердить объявление продажи как админ"""
        with self.connection:
            return self.cursor.execute("UPDATE `announcements_sell` SET `allow_admin` = ? WHERE `id` =?",
                                       (True, id_conf))

    def confirm_announcements_rent_admin(self, id_conf):
        """Подтвердить объявление аренды как админ"""
        with self.connection:
            return self.cursor.execute("UPDATE `announcements_rent` SET `allow_admin` = ? WHERE `id` =?",
                                       (True, id_conf))

    def dell_an_rent_admin(self, an_id):
        """Добавляем нового юзера"""
        with self.connection:
            return self.cursor.execute("DELETE FROM `announcements_rent` WHERE `id` =?", (an_id))

    def dell_an_sell_admin(self, an_id):
        """Добавляем нового юзера"""
        with self.connection:
            return self.cursor.execute("DELETE FROM `announcements_sell` WHERE `id` =?", (an_id))

    def why_get_admin(self, user_id) -> bool:
        """Проверка на админку"""
        with self.connection:
            return self.cursor.execute("SELECT `admin` FROM `users` WHERE `tg_id` =?", (user_id,)).fetchone()[0]

    def get_admin(self, user_id, allow_admin) -> list:
        """Выдача админки"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `admin` = ? WHERE `tg_id` =?", (allow_admin, user_id))

    def admin_all_announcements_rent(self, ):
        """Показать все объявления по аренде для админа"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_rent` WHERE `allow_admin` = ? and `allow` = ?",
                                       (False, True,)).fetchall()

    def admin_all_announcements_sell(self, ):
        """Показать все объявления по продаже для админа"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `announcements_sell` WHERE `allow_admin` = ? and `allow` = ?",
                                       (False, True,)).fetchall()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
