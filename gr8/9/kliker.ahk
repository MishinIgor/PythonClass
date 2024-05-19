;Изначально скрипт выключен
ScriptEnabled := 0

Numpad1:: ;При нажатии на клавишу Numpad1
{
    ;Инвертируем состояние скриптов (включен/выключен)
    ScriptEnabled := !ScriptEnabled
    
    ; Если скрипт включен начинаем кликать мышью
    if (ScriptEnabled) {
        Tooltip, Скрипт включен - клик мыши начнется
        SetTimer, ClickMouse, 400 ; Установка таймера
    }
    else {
        Tooltip, Скрипт выключен - клик мыши остановлен
        SetTimer, ClickMouse, off ; Остановка таймера
    }
}

ClickMouse:
{
    Click ; Кликаем
    return
}