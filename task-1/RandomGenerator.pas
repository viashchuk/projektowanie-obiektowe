program RandomGenerator;

const
  array_size = 50;
  min = 0;
  max = 100; 

type
    numbers = array[1..array_size] of Integer; 
var
    random_numbers: numbers;
    j: integer;

procedure GenerateRandomNumbers;
var 
    x, i: integer;

begin
    randomize;

    for i := 1 to array_size do begin
        x := random(max-min+1) + min;
        random_numbers[i] := x
    end;
end;


procedure QuickSort(l, r: Integer);
var 
  newL, newR: Integer;
  temp, pivot: Integer;
begin
  newL := l;
  newR := r;
  
  pivot := random_numbers[(l + r) div 2];
  
  repeat
    while random_numbers[newL] < pivot do
      newL := newL + 1;

    while random_numbers[newR] > pivot do
      newR := newR - 1;

    if newL <= newR then
    begin
      { Исправление обмена элементов }
      temp := random_numbers[newL];
      random_numbers[newL] := random_numbers[newR];
      random_numbers[newR] := temp;

      newL := newL + 1;
      newR := newR - 1;
    end;
  until newL > newR;

  if l < newR then
    QuickSort(l, newR);

  if newL < r then
    QuickSort(newL, r);
end;


begin
    GenerateRandomNumbers;
    QuickSort(1, array_size);

    for j:= 1 to array_size do
        write(random_numbers[j], ' ');
end.