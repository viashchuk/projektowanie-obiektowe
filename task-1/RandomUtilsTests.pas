
unit RandomUtilsTests;

interface

uses
  TestFramework,
  RandomUtils,
  SysUtils;

type
   TestsRandomUtils = class(TTestCase)
   published    
      procedure TestZeroArraySize;
      procedure TestArrayGeneration;
      procedure TestRandomNumberGeneration;
      procedure TestArraySorting;
      procedure TestArrayWithDuplicatesSorting;
   end;

procedure RegisterTests;

implementation

procedure RegisterTests;
begin
   TestFramework.RegisterTest(TestsRandomUtils.Suite);
end;

procedure TestsRandomUtils.TestZeroArraySize;
var
  random_numbers: IntArray;
  array_size, min, max: Integer;
begin
  array_size := 0;
  min := 1;
  max := 30;
  
  SetLength(random_numbers, array_size);

  StartExpectingException(Exception); 
  GenerateRandomNumbers(random_numbers, array_size, min, max);
  StopExpectingException();
end;

procedure TestsRandomUtils.TestArrayGeneration;
var
  random_numbers: IntArray;
  array_size: Integer;
begin
  array_size := 15;
  SetLength(random_numbers, array_size);

  CheckEquals(array_size, Length(random_numbers));
end;

procedure TestsRandomUtils.TestRandomNumberGeneration;
var
  random_numbers: IntArray;
  array_size, min, max, i: Integer;
  inRange: Boolean;
begin
  array_size := 15;
  min := 1;
  max := 30;

  SetLength(random_numbers, array_size);
  GenerateRandomNumbers(random_numbers, array_size, min, max);

  inRange := True;
  for i := 0 to array_size - 1 do
    if (random_numbers[i] < min) or (random_numbers[i] > max) then
      inRange := False;
  
  Check(inRange, 'Some generated numbers are outside the specified range');
end;

procedure TestsRandomUtils.TestArraySorting;
var
  random_numbers: IntArray;
  array_size, i, min, max: Integer;
  isSorted: Boolean;
begin
  array_size := 10;
  min := 1;
  max := 60;

  SetLength(random_numbers, array_size);
  GenerateRandomNumbers(random_numbers, array_size, min, max);
  
  QuickSort(random_numbers, 0, array_size - 1);
  
  isSorted := True;
  for i := 0 to array_size - 2 do
    if random_numbers[i] > random_numbers[i + 1] then
      isSorted := False;
  
  Check(isSorted, 'Array should sorted after QuickSort');
end;

procedure TestsRandomUtils.TestArrayWithDuplicatesSorting;
var
  random_numbers: IntArray;
  array_size, i: Integer;
  isSorted: Boolean;
begin
  array_size := 3;
  SetLength(random_numbers, array_size);
  
  random_numbers[0] := 5;
  random_numbers[1] := 3;
  random_numbers[2] := 5;
  
  QuickSort(random_numbers, 0, array_size - 1);
  
  isSorted := True;
  for i := 0 to array_size - 2 do
    if random_numbers[i] > random_numbers[i + 1] then
      isSorted := False;
  
  Check(isSorted, 'Array with duplicates should be sorted correctly');
  
  Check(random_numbers[0] = 3, 'First element should be 3');
  Check(random_numbers[1] = 5, 'Second element should be 5');
  Check(random_numbers[2] = 5, 'Third element should be 5');
end;


initialization
end.
