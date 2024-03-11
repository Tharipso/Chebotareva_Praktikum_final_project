# Ольга Чеботарева, 14-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

def post_new_order(): # функция создает новый заказ
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.create_order_body
                        )
def get_order_by_track(track): # функция получает информацию о заказе по треку
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + "?t=" + track)

def test_getting_order_by_track(): # тест проверяет статус-ответ при запросе информации о заказе по треку
    new_order= post_new_order()
    track = str(new_order.json()["track"])
    get_order_response = get_order_by_track(track)
    assert get_order_response.status_code == 200
