

-- Запросы к таблице country:

-- 1. Вывести названия всех стран Евразии
select name 
from country 
where continent in ("Europe", "Asia");

 
-- 2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет
select name, region
from country 
where LifeExpectancy < 50;

-- 3. Вывести название самой крупной по площади страны Африки
select name 
from country 
where continent = "Africa"
order by SurfaceArea DESC limit 1;


-- 4. Вывести названия пяти азиатских стран с самой низкой плотностью населения
select name 
from country 
where continent = "Asia" 
order by population ASC limit 5;



-- Запросы к таблице city

-- 5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять миллионов человек
select Name, CountryCode
from city 
where  Population > 5000000
order by population ASC;


-- 6. Вывести название города в Индии с самым длинным названием
    -- для подсчёта количества символов используйте встроенную функцию char_length()

select Name
from city 
where  CountryCode = "IND"
order by char_length(Name) DESC limit 1;


