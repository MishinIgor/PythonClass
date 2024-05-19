ScriptEnabled := 0
Numpad1:: ;При нажатии на клавишу NumPad1
{
    ; Инвертируем состояние скрипта (включаем/выключаем)
    ScriptEnabled := !ScriptEnabled

    ;Если скрипт включен, начинаем кликать мышью
    if (ScriptEnabled) {
        Tooltip, Скрипт включен - клик мыши начнется
        SetTimer, ClickMouse, 500 ;Запускаем таймер с интервалом 500 миллисекунд
    }
    else {
        Tooltip, Скрипт выключен - клик мыши остановлен
        SetTimer, ClickMouse, off ; Останавливаем таймер
    }
    return

    ClickMouse: ; Фукнция для клика мышью
    {
        Click ; Кликаем
        return
    }
}