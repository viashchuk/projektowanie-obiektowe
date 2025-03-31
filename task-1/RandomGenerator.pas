program RandomGenerator;

type
    numbers = array[integer] of 1..50;
var
    random_numbers: numbers;
    j: integer;

procedure GenerateRandomNumbers;
var 
    x, i: integer;

begin
    randomize;

    for i := 1 to 50 do begin
        x := random(100-0+1) + 0;
        random_numbers[i] := x
    end;
end;


begin
    GenerateRandomNumbers;

    for j:= 1 to 50 do
        write(random_numbers[j], ' ');
end.