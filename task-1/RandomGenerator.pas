program RandomGenerator;

type
    IntArray = array of Integer; 
var
    random_numbers: IntArray;
    array_size, min, max: Integer;
    j: integer;

procedure GenerateRandomNumbers;
var 
    x, i: integer;

begin
    randomize;

    for i := 0 to array_size - 1 do begin
        x := random(max-min+1) + min;
        random_numbers[i] := x
    end;
end;


procedure QuickSort(l, r: Integer);
var
  newL, newR, pivot, temp: Integer;
begin
  newL := l;
  newR := r;
  pivot := random_numbers[(l + r) div 2];
  
  repeat
    while random_numbers[newL] < pivot do Inc(newL);
    while random_numbers[newR] > pivot do Dec(newR);
    
    if newL <= newR then
    begin
      temp := random_numbers[newL];
      random_numbers[newL] := random_numbers[newR];
      random_numbers[newR] := temp;
      Inc(newL);
      Dec(newR);
    end;
  until newL > newR;
  
  if l < newR then QuickSort(l, newR);
  if newL < r then QuickSort(newL, r);
end;

function GetArraySize(): Integer;
var
  value: Integer;
begin
  repeat
    Write('Enter the number of numbers to generate: ');
    ReadLn(value);
    
    if value <= 0 then
      WriteLn('Error: the number must be positive');
    until value > 0;
  
  GetArraySize := value;
end;

function GetMinValue(): Integer;
var
  value: Integer;
begin
  Write('Enter the minimum random value (from): ');
  ReadLn(value);
  GetMinValue := value;
end;

function GetMaxValue(min: Integer): Integer;
var
  value: Integer;
begin
  repeat
    Write('Enter the maximum value of the random (to): ');
    ReadLn(value);
    
    if value <= min then
      WriteLn('Error: maximum value must be greater than minimum ');
    until value > min;
  
  GetMaxValue := value;
end;

begin
  array_size := GetArraySize();
  min := GetMinValue();
  max := GetMaxValue(min);

  WriteLn(min);
  WriteLn(max);
  
  SetLength(random_numbers, array_size);

  GenerateRandomNumbers;
  QuickSort(0, array_size-1);
  
  for j:= 0 to array_size-1 do
    write(random_numbers[j], ' ');
end.