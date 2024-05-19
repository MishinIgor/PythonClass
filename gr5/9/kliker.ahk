; Изначально скрипт выключен
ScriptEnabled := 0

Numpad1:: ; При нажатии на NumPad1 
{
;Инвертируем состояние скрипта (включаем/выключаем)
ScriptEnabled := !ScriptEnabled

; Если скрипт включен, начинаем кликать мышью
if (ScriptEnabled) {
    Tooltip, Скрипт включен - клик мыши начнется
    SetTimer, ClickMouse, 400 ; Запускаем таймер с интервалом 500 миллисекунд
}
else {
    Tooltip, скрипт выключен - клик мыши останавливаем
    SetTimer, ClickMouse, off ;Остановить таймер
}
}

ClickMouse: ;Функция для клика мышью
{
    Click ;Кликаем
    return
}