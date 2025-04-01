program RandomGenerator;

uses 
  RandomUtils;

var
    random_numbers: IntArray;
    array_size, min, max: Integer;

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
  
  SetLength(random_numbers, array_size);

  GenerateRandomNumbers(random_numbers, array_size, min, max);
  PrintArray(random_numbers, 'Generated numbers:');

  QuickSort(random_numbers, 0, array_size - 1);
  PrintArray(random_numbers, 'Sorted numbers:');
end.