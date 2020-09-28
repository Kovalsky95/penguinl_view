import psycopg2;
class P_db:

    # выполнение взаимодействия с базой данных пользователей "начавших общение"
    def connect_to_db(app):
        """
            Соединение с базой данных - открытие
            соединия и создание "курсора".
        """
        app.conn = psycopg2.connect(
            host="ec2-79-125-4-44.eu-west-1.compute.amazonaws.com",
            database="d4gh86bmbo44a3",
            user="svnlghwnrd44dt",
            password="8684c48054644cb06ee7ea4bc3116909bcb6cd4faaa794891444141914517e20"
        );
        app.p_user_db = app.conn.cursor();

    def init_db(app):
        """
            Инициализация базы данных - создание таблицы
            с главной информацией об "общающихся
            пользователях" при её отстутствии.
        """
        app.p_user_db.execute("""
            create table if not exists Persons(
                PersonID integer,
                reg_date timestamp
            );"""
        );
        app.commit_changes_db();

    def commit_changes_db(app):
        """
            Подтверждение действия в базе данных, такого как,
            например, добавление нового пользователя.
        """
        app.conn.commit();

    def disconnect_user_db(app):
        """
            Закрытие соединения с базой данных и удаление
            "курсора", во избежание "подвешенного
            подключения" в ожидании происходящего.
        """
        app.p_user_db.close();
        app.conn.close();
        app.p_user_db = "";
        app.conn = "";

    #инициализация экземпляра класса P_db
    def __init__(app):
        """
            .
        """
        app.connect_to_db();
        app.init_db();
        app.disconnect_user_db();
