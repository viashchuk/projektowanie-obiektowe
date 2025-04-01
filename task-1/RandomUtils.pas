
unit RandomUtils;

interface

uses
  SysUtils;

type
  IntArray = array of Integer;
  EInvalidArgument = Exception;

procedure GenerateRandomNumbers(var random_numbers: IntArray; array_size, min, max: Integer);
procedure QuickSort(var random_numbers: IntArray; l, r: Integer);
procedure PrintArray(var random_numbers: IntArray; promptMessage: String);

implementation

procedure GenerateRandomNumbers(var random_numbers: IntArray; array_size, min, max: Integer);
var 
    x, i: integer;

begin
    randomize;

   if array_size <= 0 then
      raise EInvalidArgument.create('Error: the number must be positive');

    for i := 0 to array_size - 1 do begin
        x := random(max-min+1) + min;
        random_numbers[i] := x
    end;
end;


procedure QuickSort(var random_numbers: IntArray; l, r: Integer);
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
  
  if l < newR then QuickSort(random_numbers, l, newR);
  if newL < r then QuickSort(random_numbers, newL, r);
end;

procedure PrintArray(var random_numbers: IntArray; promptMessage: String);
var
  i: Integer;
begin
  WriteLn(promptMessage);
  for i := 0 to Length(random_numbers) - 1 do
    Write(random_numbers[i], ' ');
  WriteLn;
end;

initialization
end.
