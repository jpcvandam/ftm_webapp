program FTM;

{$APPTYPE CONSOLE}

uses
  SysUtils,
  Math;

CONST
   np1 = 40000;
   np2 = 400;

TYPE
   longarray = ARRAY [1..np1] OF extended;
   shortarray = ARRAY [1..np2] OF extended;
var
  narr     : integer;
  logfile  : String;
  fileinn  : String;
  outn     : String;
  nyears: integer;
//  fileoutn, path: string;

procedure writelog(arg1, arg2: string);
var
  log : textfile;
begin
  AssignFile(log,logfile);
  if fileexists(logfile) then begin
    Append(log);
  end else
  begin
    Rewrite(log);
  end;

  writeln(log,DateTimeToStr(Now),' - ',arg1,' - ',arg2);

  CloseFile(log);
end;

PROCEDURE showmessage(arg: string);
begin
  // doe maar niks
end;
{**************************************************************************}
{PROCEDURE qcksrtlong(n: integer; VAR arr: glarray)                                           }
{**************************************************************************}
PROCEDURE qcksrtlong(n: integer; var arr: longarray);
(* Programs using routine qcksrtlong must define the type
TYPE
   glarray = ARRAY [1..np] OF real;
in the main routine, with np >= n.   *)
LABEL 11,21,22,30,99;
CONST
   m=7;
   nstack=50;
   fm=7875;
   fa=211.0;
   fc=1663.0;
VAR
   l,jstack,j,ir,iq,i: integer;
   fx,fmi,a: real;
   istack: ARRAY[1..nstack] OF integer;
BEGIN
   fmi := 1.0/fm;
   jstack := 0;
   l := 1;
   ir := n;
   fx := 0.0;
   WHILE true DO BEGIN
      IF ((ir-l) < m) THEN BEGIN
         FOR j := l+1 TO ir DO BEGIN
            a := arr[j];
            FOR i := j-1 DOWNTO 1 DO BEGIN
               IF (arr[i] <= a) THEN GOTO 11;
               arr[i+1] := arr[i]
            END;
            i := 0;
11:            arr[i+1] := a
         END;
         IF (jstack = 0) THEN GOTO 99;
         ir := istack[jstack];
         l := istack[jstack-1];
         jstack := jstack-2
      END ELSE BEGIN
         i := l;
         j := ir;
         fx := (fx*fa+fc)/fm;
         fx := fx-trunc(fx);
         iq := l+(ir-l+1)*trunc(fx*fmi);
         a := arr[iq];
         arr[iq] := arr[l];
21:         IF (j > 0) THEN BEGIN
            IF (a < arr[j]) THEN BEGIN
               j := j-1;
               GOTO 21
            END
         END;
         IF (j <= i) THEN BEGIN
            arr[i] := a;
            GOTO 30
         END;
         arr[i] := arr[j];
         i := i+1;
22:         IF (i <= n) THEN IF (a > arr[i]) THEN BEGIN
            i := i+1;
            GOTO 22
         END;
         IF (j <= i) THEN BEGIN
            arr[j] := a;
            i := j;
            GOTO 30
         END;
         arr[j] := arr[i];
         j := j-1;
         GOTO 21;
30:         jstack := jstack+2;
         IF (jstack > nstack) THEN BEGIN
            writeln('pause in qcksrtlong - NSTACK must be made larger'); readln
         END;
         IF ((ir-i) >= (i-l)) THEN BEGIN
            istack[jstack] := ir;
            istack[jstack-1] := i+1;
            ir := i-1
         END ELSE BEGIN
            istack[jstack] := i-1;
            istack[jstack-1] := l;
            l := i+1
         END
      END
   END;
99:   END;
{**************************************************************************}
{PROCEDURE qcksrtlong(n: integer; VAR arr: glarray)                                           }
{**************************************************************************}
PROCEDURE qcksrtshort(n: integer; var arr: shortarray);
(* Programs using routine qcksrtlong must define the type
TYPE
   glarray = ARRAY [1..np] OF real;
in the main routine, with np >= n.   *)
LABEL 11,21,22,30,99;
CONST
   m=7;
   nstack=50;
   fm=7875;
   fa=211.0;
   fc=1663.0;
VAR
   l,jstack,j,ir,iq,i: integer;
   fx,fmi,a: real;
   istack: ARRAY[1..nstack] OF integer;
BEGIN
   fmi := 1.0/fm;
   jstack := 0;
   l := 1;
   ir := n;
   fx := 0.0;
   WHILE true DO BEGIN
      IF ((ir-l) < m) THEN BEGIN
         FOR j := l+1 TO ir DO BEGIN
            a := arr[j];
            FOR i := j-1 DOWNTO 1 DO BEGIN
               IF (arr[i] <= a) THEN GOTO 11;
               arr[i+1] := arr[i]
            END;
            i := 0;
11:            arr[i+1] := a
         END;
         IF (jstack = 0) THEN GOTO 99;
         ir := istack[jstack];
         l := istack[jstack-1];
         jstack := jstack-2
      END ELSE BEGIN
         i := l;
         j := ir;
         fx := (fx*fa+fc)/fm;
         fx := fx-trunc(fx);
         iq := l+(ir-l+1)*trunc(fx*fmi);
         a := arr[iq];
         arr[iq] := arr[l];
21:         IF (j > 0) THEN BEGIN
            IF (a < arr[j]) THEN BEGIN
               j := j-1;
               GOTO 21
            END
         END;
         IF (j <= i) THEN BEGIN
            arr[i] := a;
            GOTO 30
         END;
         arr[i] := arr[j];
         i := i+1;
22:         IF (i <= n) THEN IF (a > arr[i]) THEN BEGIN
            i := i+1;
            GOTO 22
         END;
         IF (j <= i) THEN BEGIN
            arr[j] := a;
            i := j;
            GOTO 30
         END;
         arr[j] := arr[i];
         j := j-1;
         GOTO 21;
30:         jstack := jstack+2;
         IF (jstack > nstack) THEN BEGIN
            writeln('pause in qcksrtlong - NSTACK must be made larger'); readln
         END;
         IF ((ir-i) >= (i-l)) THEN BEGIN
            istack[jstack] := ir;
            istack[jstack-1] := i+1;
            ir := i-1
         END ELSE BEGIN
            istack[jstack] := i-1;
            istack[jstack-1] := l;
            l := i+1
         END
      END
   END;
99:   END;
{**************************************************************************}
{PROCEDURE sort2(n: integer;VAR ra,rb: glsarray);                          }
{**************************************************************************}
PROCEDURE sort2(n: integer;VAR ra,rb: shortarray);
(* Programs using routine SORT2 must define type
TYPE
   glsarray = ARRAY [1..np] OF real;
in the main routine, with np >= n.   *)
LABEL 99;
VAR
   l,j,ir,i: integer;
   rrb,rra: real;
BEGIN
   l := (n DIV 2)+1;
   ir := n;
   WHILE true DO BEGIN
      IF (l > 1) THEN BEGIN
         l := l-1;
         rra := ra[l];
         rrb := rb[l]
      END ELSE BEGIN
         rra := ra[ir];
         rrb := rb[ir];
         ra[ir] := ra[1];
         rb[ir] := rb[1];
         ir := ir-1;
         IF (ir = 1) THEN BEGIN
            ra[1] := rra;
            rb[1] := rrb;
            GOTO 99
         END
      END;
      i := l;
      j := l+l;
      WHILE (j <= ir) DO BEGIN
         IF (j < ir) THEN
            IF (ra[j] < ra[j+1]) THEN j := j+1;
         IF (rra < ra[j]) THEN BEGIN
            ra[i] := ra[j];
            rb[i] := rb[j];
            i := j;
            j := j+j
         END ELSE j := ir+1
      END;
      ra[i] := rra;
      rb[i] := rrb
   END;
99:   END;
{**************************************************************************}
{PROCEDURE statisticslong(data: longarray; n: integer; VAR ave,svar: real);                                           }
{**************************************************************************}
PROCEDURE statisticslong(data: longarray; n: integer;
       VAR min,max,ave,adev,sdev,svar,skew,curt: real);
(* Programs using routine MOMENT must define the type
TYPE
   longarray = ARRAY [1..n] OF real;
in the calling routine *)
VAR
   j: integer;
   s,p: real;
BEGIN
   IF (n <= 1) THEN BEGIN
      writeln('pause in MOMENT - n must be at least 2'); readln
   END;
   s := 0.0;
   FOR j := 1 TO n DO s := s+data[j];
   qcksrtlong(n,data);
   min := data[1];
   max := data[n];
   //ave := s/n;
   adev := 0.0;
   svar := 0.0;
   skew := 0.0;
   curt := 0.0;
   FOR j := 1 TO n DO BEGIN
      s := data[j]-ave;
      adev := adev+abs(s);
      p := s*s;
      svar := svar+p;
      p := p*s;
      skew := skew+p;
      p := p*s;
      curt := curt+p
   END;
   adev := adev/n;
   svar := svar/(n-1);
   sdev := sqrt(svar);
//   IF (svar <> 0.0) THEN BEGIN
//      skew := skew/(n*sdev*sdev*sdev);
//      curt := curt/(n*sqr(svar))-3.0
//   END ELSE BEGIN
//      writeln('pause in MOMENT - no skew/kurtosis when variance = 0'); readln
//   END
END;
{**************************************************************************}
{PROCEDURE statisticslong(data: longarray; n: integer; VAR ave,svar: real);                                           }
{**************************************************************************}
PROCEDURE statisticsshort(data: shortarray; n: integer;
       VAR min,max,ave,adev,sdev,svar,skew,curt: real);
(* Programs using routine MOMENT must define the type
TYPE
   longarray = ARRAY [1..n] OF real;
in the calling routine *)
VAR
   j: integer;
   s,p: real;
BEGIN
   IF (n <= 1) THEN BEGIN
      writeln('pause in MOMENT - n must be at least 2'); readln
   END;
   s := 0.0;
   FOR j := 1 TO n DO s := s+data[j];
   qcksrtshort(n,data);
   min := data[1];
   max := data[n];
   ave := s/n;
   adev := 0.0;
   svar := 0.0;
   skew := 0.0;
   curt := 0.0;
   FOR j := 1 TO n DO BEGIN
      s := data[j]-ave;
      adev := adev+abs(s);
      p := s*s;
      svar := svar+p;
      p := p*s;
      skew := skew+p;
      p := p*s;
      curt := curt+p
   END;
   adev := adev/n;
   svar := svar/(n-1);
   sdev := sqrt(svar);
//   IF (svar <> 0.0) THEN BEGIN
//      skew := skew/(n*sdev*sdev*sdev);
//      curt := curt/(n*sqr(svar))-3.0
//   END ELSE BEGIN
//      writeln('pause in MOMENT - no skew/kurtosis when variance = 0'); readln
//   END
END;
{**************************************************************************}
{Hydrological functions gt: ghg                                    }
{**************************************************************************}
Procedure xarray(fileinn: string; VAR xarr: longarray );// stdcall;
{ procedure to calculate the ghg }
{$i+}
Var
  filein: textfile;
  line: string;
  level: real;
  i: integer;
begin
 // fileinn:='c:\wmtools\delphy\dll\44FP7603.01';
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file c:\wmtools\etc\neerslag.dat does not exists');
      exit
    end;
  reset(filein);
  i:=0; narr:=0;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
//     day   := StrToInt (Copy(line,1,2));
//     month  := StrToInt (Copy(line,4,2));
//     year  := StrToInt (Copy(line,7,2));
     level  := StrToFloat (Copy(line,10,7));
 // ShowMessage (format(' level = %8.2f', [level]));
     narr := narr+1;
     i:=i+1;
     xarr[i]:=level;
   end;
  closefile(filein);
end;
{**************************************************************************}
{Hydrological functions gt: ghg                                    }
{**************************************************************************}
Procedure duurlijn(fileinn,fileoutn: string);// stdcall;
{ procedure to calculate the ghg }
{$i+}
Var
  filein,fileout: textfile;
  line: string;
  y,index,day,month,x: real;
  arrduurlijn:longarray;
  i: integer;     //,nyears
begin
 // fileinn:='c:\wmtools\delphy\dll\44FP7603.01';
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file ..... does not exists');
      exit
    end;
  reset(filein);
  AssignFile (fileout,fileoutn); Rewrite (fileout);
  i:=0; narr:=0; day:=0; month:=0;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
     if ((day = 29) and (month = 2)) then readln(filein,line);
     day   := StrToInt (Copy(line,1,2));
     month  := StrToInt (Copy(line,4,2));
//     year  := StrToInt (Copy(line,7,2));
     x  := StrToFloat (Copy(line,10,7));
     narr := narr+1;
     i:=i+1;
     arrduurlijn[i]:=x*-1;
   end;
  nyears := floor(narr/365);
  qcksrtlong(narr,arrduurlijn);
    for i := 1 to narr do begin
      index:=i/nyears;
      y:=arrduurlijn[i]*-1;
      writeln (fileout,format('%8.3f',[index]),format('%8.2f',[y]));
    end;
  closefile(filein);
  closefile(fileout);
end;
{**************************************************************************}
{Hydrological functions gt: ghg                                    }
{**************************************************************************}
function overschrijding(fileinn: string; o: real): real; stdcall;
{ procedure to calculate the ghg }
{$i+}
Var
  filein: textfile;
  line: string;
  day,month,x,y: real;
  arroverschrijding:longarray;
  i,k,nyears: integer;
begin
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file ..... does not exists');
      exit
    end;
  reset(filein);
  i:=0; k:=0; narr:=0; day:=0; month:=0;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
     if ((day = 29) and (month = 2)) then readln(filein,line);
     day   := StrToInt (Copy(line,1,2));
     month  := StrToInt (Copy(line,4,2));
     x  := StrToFloat (Copy(line,10,7));
     narr := narr+1;
     i:=i+1;
     arroverschrijding[i]:=x*-1;
   end;
  nyears := floor(narr/365);
  qcksrtlong(narr,arroverschrijding);
    for i := 1 to narr do begin
      y:=arroverschrijding[i]*-1;
      if y >= o then k:=k+1;
    end;
  overschrijding:=k/nyears;
  closefile(filein);
end;
{**************************************************************************}
{Hydrological functions gt: ghg                                    }
{**************************************************************************}
function xoverschrijding(fileinn: string; o: real): real; stdcall;
{ procedure to calculate the overschrijdingsduren }
{$i+}
Var
  filein: textfile;
  line: string;
  day,month,x: real;
  arroverschrijding:longarray;
  i,nyears: integer;
begin
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file ..... does not exists');
      exit
    end;
  reset(filein);
  i:=0; narr:=0; day:=0; month:=0;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
     if ((day = 29) and (month = 2)) then readln(filein,line);
     day   := StrToInt (Copy(line,1,2));
     month  := StrToInt (Copy(line,4,2));
     x  := StrToFloat (Copy(line,10,7));
     narr := narr+1;
     i:=i+1;
     arroverschrijding[i]:=x*-1;
   end;
  nyears := floor(narr/365);
  qcksrtlong(narr,arroverschrijding);
//    for i := 1 to narr do begin
//      y:=arroverschrijding[i]*-1;
//      if y >= o then k:=k+1;
//    end;
  i := floor(o*nyears);
  xoverschrijding:=arroverschrijding[i]*-1;
  closefile(filein);
end;
{**************************************************************************}
{Hydrological functions gt: ghg                                    }
{**************************************************************************}
Procedure regimecurve(fileinn,fileoutn: string);// stdcall;
{ procedure to calculate the regimecurve }
{$i+}
const
  prob = 1.96;
Var
  filein,fileout: textfile;
  line: string;
  day,month,x: real;
  min,max,ave,adev,sdev,svar,skew,curt: real;
  arrx:longarray;
  arrregime,regimearr,regime5arr,regime95arr:shortarray;
  i,j,k,nyears: integer;
begin
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file ..... does not exists');
      exit
    end;
  reset(filein);
  AssignFile (fileout,fileoutn); Rewrite (fileout);
  writeln (fileout,'# dag  regime      5%     95%');
  i:=0; narr:=0; day:=0; month:=0;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
     if ((day = 29) and (month = 2)) then readln(filein,line);
     day   := StrToInt (Copy(line,1,2));
     month  := StrToInt (Copy(line,4,2));
//     year  := StrToInt (Copy(line,7,2));
     x  := StrToFloat (Copy(line,10,7));
     narr := narr+1;
     i:=i+1;
     arrx[i]:=x;
   end;
  nyears := floor(narr/365);
    for k := 1 to 365 do begin
      for j := 1 to nyears do begin
        i:=k+((j-1)*365);
        arrregime[j]:=arrx[i];
      end;
      statisticsshort(arrregime,nyears,min,max,ave,adev,sdev,svar,skew,curt);
      regimearr[k]:=ave;
      regime5arr[k]:=ave-(prob*sdev);
      regime95arr[k]:=ave+(prob*sdev);
    end;
    for i := 1 to 365 do begin
      writeln (fileout,format('%5d',[i]),format('%8.2f',[regimearr[i]])
               ,format('%8.2f',[regime5arr[i]]),format('%8.2f',[regime95arr[i]]));
    end;
  closefile(filein);
  closefile(fileout);
end;
{**************************************************************************}
{**************************************************************************}
{Hydrological functions gt: ghg                                    }
{**************************************************************************}
Procedure ghgarray(fileinn: string; VAR ghgarr: shortarray );// stdcall;
{ procedure to calculate the ghgarray }
{$i+}
Var
  filein: textfile;
  line: string;
  firstyear,hg3,year,day,month,datum,level: extended;
  arrlevel,arrdatum:shortarray;
  i,j,k,l,nt: integer;
  winter:boolean;
begin
 // fileinn:='c:\wmtools\delphy\dll\44FP7603.01';
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file c:\wmtools\etc\neerslag.dat does not exists');
      exit
    end;
  reset(filein);
 //
  firstyear:=1900;
  i:=0; j:=0; k:=0; l:=0; narr:=0; datum :=0;
  winter:=False;
  WHILE not eof(filein) DO
   BEGIN
//     ShowMessage (format (' i = %d', [i]));
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
 //    ShowMessage (line);
//     readln(filein,line);
     day   := StrToInt (Copy(line,1,2));
     month  := StrToInt (Copy(line,4,2));
     year  := StrToInt (Copy(line,7,2));
     datum := (day * 10000) + (month * 100) + year;
     level  := StrToFloat (Copy(line,9,8));
     if (j = 0) then firstyear:=year;
     if (day = 31) and (month = 3) then winter:=False;
     if (day = 1) and (month = 4) then
//     if ((month > 3) and (year = firstyear))then
      begin
        winter:=True;
        for j := 1 to np2 do
          begin
           arrlevel[j]:=0.0;
           arrdatum[j]:=0.0;
          end;
        j:=1;
        l:=1;
      end;
//     if ((month < 4) and (year <> firstyear)) then
//      begin
//        winter:=True;
//        j:=1;
//        l:=1;
//      end;
     if ((winter = true) and ((day = 14) or (day = 28))) then
      Begin
        i:=i+1;
        arrlevel[i]:=level*-1;
        arrdatum[i]:=datum
//  ShowMessage (format(' day = %8.2f', [day]));
//  ShowMessage (format(' level = %8.2f', [level]));
//       ShowMessage (format(' arrlevel = %10.5f', [arrlevel[i]]));
      end;
     if (winter = false) then
      begin
        j:=j+1;
      end;
     if ((winter = false) and (year <> firstyear)) then
      Begin
        narr := narr+1;
//  ShowMessage (format('n%d',[n]));
 //   m:=7;
        k   := k+1;
        nt   := i;
        sort2(nt,arrlevel,arrdatum);
//        qcksrtlong(nt,arrlevel);
        hg3:=(arrlevel[1]+arrlevel[2]+arrlevel[3])/3;
        ghgarr[k]:=hg3*-1;
        i:=0;
      end;
   end;
  closefile(filein);
end;
{**************************************************************************}
{**************************************************************************}
{Hydrological functions gt: glg                                    }
{**************************************************************************}
Procedure gvgarray(fileinn: string; VAR gvgarr: shortarray );// stdcall;
{ function to calculate the gvgarray }
{$i+}
Var
  filein: textfile;
  line: string;
  vg3,firstyear,year,day,month,level,datum: extended;
  arrlevel,arrdatum:shortarray;
  i,j,k,l: integer;
  voorjaar:boolean;
begin
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file ...... does not exists');
      exit
    end;
  reset(filein);
 //
  i:=0; j:=0; k:=0; l:=0; narr:=0;
  voorjaar:=False;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
     day   := StrToInt (Copy(line,1,2));
     month  := StrToInt (Copy(line,4,2));
     year  := StrToInt (Copy(line,7,2));
     datum := (day * 10000) + (month * 100) + year;
     level  := StrToFloat (Copy(line,9,8));
     if (j = 0) then firstyear:=year;
     if (day = 15) and (month = 4) then voorjaar:=False;
     if (day = 15) and (month = 4) then l:=1;  //switch
     if (day = 1) and (month = 3) then
      begin
        voorjaar:=True;
        for j := 1 to np2 do
          begin
           arrlevel[j]:=0.0;
           arrdatum[j]:=0.0;
          end;
        j:=1;
        l:=1;
      end;
     if ((voorjaar = true) and ((day = 14) or (day = 28)))then
      Begin
        i:=i+1;
 // ShowMessage (format(' level = %8.2f', [level]));
        arrlevel[i]:=level;
        arrdatum[i]:=datum;
      end;
     if (voorjaar = false) and (l=1) then
      Begin
        narr   := narr+1;
        k   := k+1;
        vg3:=(arrlevel[1]+arrlevel[2]+arrlevel[3])/3;
        gvgarr[k]:=vg3;
        i:=0;
        l:=2;
      end;
   end;
  closefile(filein);
end;


{**************************************************************************}
{Hydrological functions gt: glg                                    }
{**************************************************************************}
Procedure glgarray(fileinn: string; VAR glgarr: shortarray );// stdcall;
{ function to calculate the glgarray }
{$i+}
Var
 // fileinn: string[100];
  filein,fileoutxg: textfile;
  line,fileoutxgn: string;
  firstyear,lg3,day,month,year,level,datum: extended;
  arrlevel,arrdatum:shortarray;
  i,j,k,l,nt: integer;
  summer:boolean;
begin
 // fileinn:='c:\wmtools\delphy\dll\44FP7603.01';
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file ...... does not exists');
      exit
    end;
  reset(filein);
 //
  firstyear:=1900;
  i:=0; j:=0; k:=0; l:=0; narr:=0;
  summer:=False;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
     day   := StrToInt (Copy(line,1,2));
     month  := StrToInt (Copy(line,4,2));
     year  := StrToInt (Copy(line,7,2));
     datum := (day * 10000) + (month * 100) + year;
     level  := StrToFloat (Copy(line,9,8));
//  ShowMessage (format(' level = %8.2f', [level]));
     if (j = 0) then firstyear:=year;
     if (day = 31) and (month = 3) then summer:=False;
     if (day = 1) and (month = 4) then
//     if ((month > 3) and (year = firstyear))then
      begin
        summer:=True;
        for j := 1 to np2 do
          begin
           arrlevel[j]:=0.0;
           arrdatum[j]:=0.0;
          end;
        j:=1;
        l:=1;
      end;
     if ((summer = true) and ((day = 14) or (day = 28))) then
      Begin
        i:=i+1;
        arrlevel[i]:=level;
        arrdatum[i]:=datum
      end;
     if (summer = false) then j:=j+1;
     if (summer = false) and  (year <> firstyear) then
      Begin
        narr   := narr+1;
        k   := k+1;
        nt   := i;
        sort2(nt,arrlevel,arrdatum);
//        qcksrtlong(nt,arrlevel);
        lg3:=(arrlevel[1]+arrlevel[2]+arrlevel[3])/3;
        glgarr[k]:=lg3;
        i:=0;
      end;
   end;
  closefile(filein);
end;
{**************************************************************************}
{**************************************************************************}
{Hydrological functions gt: glg                                    }
{**************************************************************************}
Procedure glgsarray(fileinn: string; VAR glgsarr: shortarray );// stdcall;
{ function to calculate the glgs }
{$i+}
Var
 // fileinn: string[100];
  filein: textfile;
  line: string;
  lg3,day,month,level: extended;
  arrlevel:longarray;
  i,j,k,l,nt: integer;
  summer:boolean;
begin
 // fileinn:='c:\wmtools\delphy\dll\44FP7603.01';
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file ...... does not exists');
      exit
    end;
  reset(filein);
//  firstyear:=1900;
  i:=0; j:=0; k:=0; l:=0; narr:=0;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
     day   := StrToInt (Copy(line,1,2));
     month  := StrToInt (Copy(line,4,2));
  //   year  := StrToInt (Copy(line,7,2));
     level  := StrToFloat (Copy(line,10,6));
//  ShowMessage (format(' level = %8.2f', [level]));
 //    if (j = 0) then firstyear:=year;
     summer:=False;
     if (month > 3 ) and (month < 10) then
      begin
        summer:=True;
        j:=1;
        l:=1;
      end;
     if ((summer = true) and ((day = 14) or (day = 28))) then
      Begin
        i:=i+1;
        arrlevel[i]:=level;
      end;
     if summer = false then l:=l+1;
     if (summer = false) and  (l = 2) and (j = 1) then
      Begin
        narr   := narr+1;
        k   := k+1;
        nt   := i;
//       ShowMessage (format(' arrlevel = %10.5f', [arrlevel[1]]));
        qcksrtlong(nt,arrlevel);
        lg3:=(arrlevel[1]+arrlevel[2]+arrlevel[3])/3;
 //       ShowMessage (format(' arrlevel = %10.5f', [arrlevel[1]]));
 //       ShowMessage (format(' arrlevel = %10.5f', [arrlevel[2]]));
 //       ShowMessage (format(' arrlevel = %10.5f', [arrlevel[3]]));
        glgsarr[k]:=lg3;
        i:=0;
 //       ShowMessage (format(' glgarr = %10.5f', [glgarr[k]]));
      end;
   end;
  closefile(filein);
end;
{**************************************************************************}
{Hydrological functions                                     }
{**************************************************************************}
Procedure q1array(fileinn: string; VAR q1arr: shortarray );// stdcall;
{ procedure to calculate the qlarray}
{$i+}
Var
  filein: textfile;
  line: string;
  j,year,qout,q1: real;
  arrq:shortarray;
  i,k,l,nt: integer;
begin
 // fileinn:='c:\wmtools\delphy\dll\44FP7603.01';
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file c:\wmtools\etc\neerslag.dat does not exists');
      exit
    end;
  reset(filein);
  i:=0; j:=0; k:=0; l:=0; narr:=0;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
     year  := StrToInt (Copy(line,7,2));
     qout  := StrToFloat (Copy(line,10,7));
     l:=l+1;
     if (l = 1) then j:=year;
     if (j = year) then
      Begin
        i:=i+1;
        arrq[i]:=qout*-1;
      end;
     if (j <> year) or eof(filein) then
      begin
        narr := narr+1;
 //   m:=7;
        k:=k+1;
        nt   := i;
        qcksrtshort(nt,arrq);
        q1:=arrq[1];
        q1arr[k]:=q1*-1;
        j:=year;
        i:=0;
      end;
   end;
  closefile(filein);
end;
{**************************************************************************}
{Hydrological functions                                     }
{**************************************************************************}
Procedure q15array(fileinn: string; VAR q15arr: shortarray );// stdcall;
{ procedure to calculate the}
{$i+}
Var
  filein: textfile;
  line: string;
  j,year,qout,q15: real;
  arrq:shortarray;
  i,k,l,nt: integer;
begin
 // fileinn:='c:\wmtools\delphy\dll\44FP7603.01';
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file c:\wmtools\etc\neerslag.dat does not exists');
      exit
    end;
  reset(filein);
  i:=0; j:=0; k:=0; l:=0; narr:=0;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
     year  := StrToInt (Copy(line,7,2));
     qout  := StrToFloat (Copy(line,10,7));
     l:=l+1;
     if (l = 1) then j:=year;
     if (j = year) then
      Begin
        i:=i+1;
        arrq[i]:=qout*-1;
      end;
     if (j <> year) or eof(filein) then
      begin
        narr := narr+1;
        k:=k+1;
        nt   := i;
        qcksrtshort(nt,arrq);
        q15:=arrq[15];
        q15arr[k]:=q15*-1;
        j:=year;
        i:=0;
 //       ShowMessage (format(' arrghg = %10.5f', [arrghg[k]]));
      end;
   end;
  closefile(filein);
end;
{**************************************************************************}
{Hydrological functions                                     }
{**************************************************************************}
Procedure q100array(fileinn: string; VAR q100arr: shortarray );// stdcall;
{ procedure to calculate the}
{$i+}
Var
  filein: textfile;
  line: string;
  j,year,qout,q100: real;
  arrq:shortarray;
  i,k,l,nt: integer;
begin
  assignfile(filein, fileinn);
  if FileExists(fileinn) then
   // ShowMessage ('ja, gevonden');
  if not FileExists(fileinn) then
    Begin
      ShowMessage ('The file c:\wmtools\etc\neerslag.dat does not exists');
      exit
    end;
  reset(filein);
  i:=0; j:=0; k:=0; l:=0; narr:=0;
  WHILE not eof(filein) DO
   BEGIN
     readln(filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
     year  := StrToInt (Copy(line,7,2));
     qout  := StrToFloat (Copy(line,10,7));
     l:=l+1;
     if (l = 1) then j:=year;
     if (j = year) then
      Begin
        i:=i+1;
        arrq[i]:=qout*-1;
      end;
     if (j <> year) or eof(filein) then
      begin
        narr := narr+1;
        k:=k+1;
        nt   := i;
        qcksrtshort(nt,arrq);
        q100:=arrq[100];
        q100arr[k]:=q100*-1;
        j:=year;
        i:=0;
 //       ShowMessage (format(' arrghg = %10.5f', [arrghg[k]]));
      end;
   end;
  closefile(filein);
end;
{**************************************************************************}
{Hydrological functions gt: gwt                                    }
{**************************************************************************}
Procedure gwt(glg,ghg: real; VAR gt,gtnr: string);// stdcall;
//FUNCTION gwt(glg,ghg: real): integer; stdcall;
{ function to calculate the ghg }
{$i+}
//Var

begin
  if (ghg > -25.0) and (glg > -50.0) then begin
     gtnr := '11';
     gt := 'Ia';
  end
  else if (ghg < -25.0) and (glg > -50.0) then begin
     gtnr := '12';
     gt := 'Ib';
  end
  else if (ghg > -25.0) and ((glg < -50.0) and (glg > -80.0)) then begin
     gtnr := '21';
     gt := 'ÃIa';
  end
  else if ((ghg < -25.0) and (ghg > -40))
         and ((glg < -50.0) and (glg > -80.0)) then begin
     gtnr := '22';
     gt := 'IIb';
  end
  else if (ghg < -40.0) and ((glg < -50.0) and (glg > -80.0)) then begin
     gtnr := '23';
     gt := 'IIc';
  end
  else if (ghg > -25.0) and ((glg < -80.0) and (glg > -120.0)) then begin
     gtnr := '31';
     gt := 'IIIa';
  end
  else if ((ghg < -25.0) and (ghg > -40))
         and ((glg < -80.0) and (glg > -120.0)) then begin
     gtnr := '32';
     gt := 'IIIb';
  end
  else if ((ghg < -40.0) and (ghg > -80.0))
         and ((glg < -80.0) and (glg > -120.0)) then begin
     gtnr := '41';
     gt := 'IVu';
  end
  else if (ghg < -80.0) and ((glg < -80.0) and (glg > -120.0)) then begin
     gtnr := '42';
     gt := 'IVc';
  end
  else if (ghg > -25.0) and (glg < -120.0) then begin
     gtnr := '51';
     gt := 'Va';
  end
  else if ((ghg < -25.0) and (ghg > -40.0))
         and (glg < -120.0) then begin
     gtnr := '52';
     gt := 'Vb';
  end
  else if ((ghg < -40.0) and (ghg > -80.0))
         and ((glg < -120.0) and (glg > -180.0)) then begin
     gtnr := '61';
     gt := 'VIo';
  end
  else if ((ghg < -40.0) and (ghg > -80.0))
         and (glg < -180.0) then begin
     gtnr := '62';
     gt := 'VId';
  end
  else if ((ghg < -80.0) and (ghg > -140.0))
         and ((glg < -120.0) and (glg > -180.0)) then begin
     gtnr := '71';
     gt := 'VIIo';
  end
  else if ((ghg < -80.0) and (ghg > -140.0))
         and (glg < -180.0) then begin
     gtnr := '72';
     gt := 'VIId';
  end
  else if (ghg < -140.0) and ((glg < -120.0) and (glg > -180.0)) then begin
     gtnr := '81';
     gt := 'VIIIo';
  end
  else if (ghg < -140.0) and (glg < -180.0) then begin
     gtnr := '82';
     gt := 'VIIId';
  end
end;
{**************************************************************************}
{Hydrological functions gt: ghg                                    }
{**************************************************************************}
PROCEDURE NLT(fileinparamn,fileinmeteon,outn: string; var fileoutn,path:string); stdcall;
//FUNCTION gwl(fileinn: shstring): real; stdcall;
{ function to calculate the ghg }
{$i+}
Var

  fileoutalln,fileoutstatn,fileduurlijnn,fileregimen: string;
  fileoutstat: textfile;
  xarr:longarray;
  ghgarr,glgarr,glgsarr,gvgarr,q1arr,q15arr,q100arr:shortarray;
  min,max,ave,adev,sdev,svar,skew,curt: real;
  glg,ghg,gvg,q1,q15,q100,overschr,xoverschr: real;
  gt,gtnr: string;


  fileoutqn: string;
  filein,fileinmeteo,fileout,fileoutq,fileoutall: textfile;
  neerslag,verdamping,neerslagoverschot:extended;
  afvoer,hgem,cw,xoverschrGLG:extended;
  day,year,month,h0,drainageweerstand,qbot:extended;
  bergingscoefficient,delta,omega,hmin1,h,aanloop:extended;
  line: string;
  i,runnr: integer;
  done:boolean;
 // const hm: extended;
BEGIN
  assignfile(filein, fileinparamn);
  if FileExists(fileinparamn) then
//    ShowMessage ('ja, gevonden');
  if not FileExists(fileinparamn) then
   Begin
     ShowMessage ('The file does not exists');
     exit
  end;
  reset(filein);
    aanloop:=0;
    hgem:=0;
    drainageweerstand:=0;
    bergingscoefficient:=0;
    qbot:=0;
//    hdiep:=0;
//    cwaarde:=0;
//    fa:=0; fb:=0; fc:=0; fd:=0;
//    a:=0;b:=0;

  fileoutalln := path+'HydroNLTresult.txt';
  AssignFile (fileoutall,fileoutalln); Rewrite (fileoutall);
  write (fileoutall,'runnr    hgem   drwst berging    qbot   delta   omega');
  writeln (fileoutall,'       c     GHG     GVG     GLG LG310%d      q1');



    WHILE not eof(filein) DO BEGIN
    Readln (filein,line);
      while line[1] = '#' do begin
        Readln (filein,line);
      end;
    runnr:= StrToInt (copy(line,1,8));
    ShowMessage ((copy(line,1,8)));
    aanloop:= StrToFloat (copy(line,9,8));
    hgem:= StrToFloat (copy(line,17,8));
    drainageweerstand:= StrToFloat (copy(line,25,8));
    bergingscoefficient:= StrToFloat (copy(line,33,8));
    qbot:= StrToFloat (copy(line,41,8));

    h0:=hgem;

  assignfile(fileinmeteo, fileinmeteon);
//  if FileExists(fileinmeteon) then
//    ShowMessage ('ja, gevonden');
  if not FileExists(fileinmeteon) then
   Begin
     ShowMessage ('The file does not exist');
     exit
  end;
  reset(fileinmeteo);
  done:=false;
  path:='';
  i:=-1; //j:=0;
  fileoutn := path+outn+'gwl.txt';
  AssignFile (fileout,fileoutn); Rewrite (fileout);
  writeln (fileout,'#   date  grwst');
  writeln (fileout,'#            cm');

  fileoutqn := path+outn+'q.txt';
  AssignFile (fileoutq,fileoutqn); Rewrite (fileoutq);
  writeln (fileoutq,'#   date      q');
  writeln (fileoutq,'#          mm/d');

{  fileoutqbotn := path+outn+'qbot.txt';
  AssignFile (fileoutqbot,fileoutqbotn); Rewrite (fileoutqbot);
  writeln (fileoutqbot,'#   date   qbot');
  writeln (fileoutqbot,'#          mm/d'); }


      Delta:= Exp( -1 /( bergingscoefficient * drainageweerstand )) ;
      Omega:=  drainageweerstand * ( 1 - delta ) ;
      cw:=  ((drainageweerstand * (qbot / 10)) * 1) + hgem;
  hmin1:= h0;
  Readln (fileinmeteo,line);
  i:=i+1;
    for i := 0 to 3650 do begin
      Readln (fileinmeteo,line);
      day:= StrToFloat (copy(line,2,4));
      month:= StrToFloat (copy(line,16,2));
      year:= StrToFloat (copy(line,32,2));
      neerslag:= StrToFloat (copy(line,44,7));
      verdamping:= StrToFloat (copy(line,58,5));
      neerslagoverschot:= neerslag - verdamping;
      h:= cw + delta * (hmin1 - cw) + omega * (neerslagoverschot / 10);
 //     correctie boven maaiveld
      if (h > 0) then h:=0;
      hmin1:= h;
     end;
    close(fileinmeteo);
//  assignfile(fileinmeteo, fileinmeteon);
  reset(fileinmeteo);
  Readln (fileinmeteo,line);

    WHILE not eof(fileinmeteo) DO BEGIN
      Readln (fileinmeteo,line);
      i:=i+1;
      day:= StrToFloat (copy(line,2,4));
      month:= StrToFloat (copy(line,16,2));
      year:= StrToFloat (copy(line,32,2));
      neerslag:= StrToFloat (copy(line,44,7));
      verdamping:= StrToFloat (copy(line,58,5));
      neerslagoverschot:= neerslag - verdamping;
      h:= cw + delta * (hmin1 - cw) + omega * (neerslagoverschot / 10);
      afvoer:= ((hgem * -1) - (h * -1))*10 / drainageweerstand;
      if (h > 0) then h:=0;
      if (afvoer < 0) then afvoer := 0;
 //     correctie boven maaiveld
      if (i > aanloop) then begin
      writeln (fileout,format('%2.0f',[day]),'-',format('%2.0f',[month]),'-',
               format('%2.0f',[year]),format('%8.1f',[h]));
      writeln (fileoutq,format('%2.0f',[day]),'-',format('%2.0f',[month]),'-',
               format('%2.0f',[year]),format('%8.1f',[afvoer]));

      end;
      hmin1:= h;
     end;
    close(fileinmeteo);
  close(fileout);
  close(fileoutq);
//  close(fileoutqbot);
 //    ShowMessage (simyear);
//  ShowMessage (fileintmpn);

  fileduurlijnn := path+outn+'gwlduurlijn.txt';
  duurlijn(fileoutn,fileduurlijnn);
  fileregimen := path+outn+'gwlregime.txt';
  regimecurve(fileoutn,fileregimen);
  //  fileduurregimen := path+outn+'gwlduurregime.txt';
  //  duurregime(fileoutn,fileduurregimen);
  fileoutstatn := path+outn+'gwlstatistics.txt';
  AssignFile (fileoutstat,fileoutstatn); Rewrite (fileoutstat);
  writeln(fileoutstat,'         ave     min     max    sdev     var oversch');
  xarray(fileoutn,xarr);
//  ShowMessage (format('narr%d',[narr]));
  statisticslong(xarr,narr,min,max,ave,adev,sdev,svar,skew,curt);
  writeln(fileoutstat,'gwl ',format('%8.1f',[ave]),
          format('%8.1f',[min]),format('%8.1f',[max]),
          format('%8.1f',[sdev]),format('%8.1f',[svar]));
//  ghgwarray(fileoutn,ghgwarr);
  ghgarray(fileoutn,ghgarr);
//  ShowMessage (format('narr%d',[narr]));
  statisticsshort(ghgarr,narr,min,max,ave,adev,sdev,svar,skew,curt);
  ghg:=ave;
  overschr:=overschrijding(fileoutn,ghg);
  writeln(fileoutstat,'ghg ',format('%8.1f',[ave]),
          format('%8.1f',[min]),format('%8.1f',[max]),
          format('%8.1f',[sdev]),format('%8.1f',[svar]),
          format('%8.1f',[overschr]));
  gvgarray(fileoutn,gvgarr);
//  ShowMessage (format('narr%d',[narr]));
  statisticsshort(gvgarr,narr,min,max,ave,adev,sdev,svar,skew,curt);
  gvg:=ave;
  overschr:=overschrijding(fileoutn,gvg);
  writeln(fileoutstat,'gvg ',format('%8.1f',[ave]),
          format('%8.1f',[min]),format('%8.1f',[max]),
          format('%8.1f',[sdev]),format('%8.1f',[svar]),
          format('%8.1f',[overschr]));
 glgsarray(fileoutn,glgsarr);
  glgarray(fileoutn,glgarr);
//  ShowMessage (format('narr%d',[narr]));
  statisticsshort(glgarr,narr,min,max,ave,adev,sdev,svar,skew,curt);
  glg:=ave;
  overschr:=overschrijding(fileoutn,glg);
  writeln(fileoutstat,'glg ',format('%8.1f',[ave]),
          format('%8.1f',[min]),format('%8.1f',[max]),
          format('%8.1f',[sdev]),format('%8.1f',[svar]),
          format('%8.1f',[overschr]));

//  fileoutxg3n := path+outn+'gwlduurlijn.txt';
//  AssignFile(fileoutxg3,fileoutxg3n); reset (fileoutxg3);
  xoverschrGLG:=xoverschrijding(fileoutn,350);
//  closefile(fileoutxg3);
  writeln(fileoutstat,'LG310%',format('%8.1f',[xoverschrGLG]));

  gwt(glg,ghg,gt,gtnr);
  writeln(fileoutstat,' ');
  writeln(fileoutstat,'gt   ',gt);
  writeln(fileoutstat,'gtnr ',gtnr);
  closefile(fileoutstat);

// Afvoer
 // qfile(fileinn,outn,fileoutn,path);
  fileduurlijnn := path+outn+'qduurlijn.txt';
  duurlijn(fileoutqn,fileduurlijnn);
  fileregimen := path+outn+'qregime.txt';
  regimecurve(fileoutqn,fileregimen);
  fileoutstatn := path+outn+'Qstatistics.txt';
  AssignFile (fileoutstat,fileoutstatn); Rewrite (fileoutstat);
  writeln(fileoutstat,'          Tp Te(ave)     min     max    sdev    svar');
  xarray(fileoutqn,xarr);
  statisticslong(xarr,narr,min,max,ave,adev,sdev,svar,skew,curt);
  writeln(fileoutstat,'q   ',format('%16.1f',[ave]),
          format('%8.1f',[min]),format('%8.1f',[max]),
          format('%8.1f',[sdev]),format('%8.1f',[svar]));
  q1array(fileoutqn,q1arr);
  statisticsshort(q1arr,narr,min,max,ave,adev,sdev,svar,skew,curt);
  q1:=ave;
  overschr:=overschrijding(fileoutqn,q1);
  xoverschr:=xoverschrijding(fileoutqn,1);
  writeln(fileoutstat,'q1  ',format('%8.1f',[xoverschr]),format('%8.1f',[ave]),
          format('%8.1f',[min]),format('%8.1f',[max]),
          format('%8.1f',[sdev]),format('%8.1f',[svar]),
          format('%8.1f',[overschr]));
  q15array(fileoutqn,q15arr);
  statisticsshort(q15arr,narr,min,max,ave,adev,sdev,svar,skew,curt);
  q15:=ave;
  overschr:=overschrijding(fileoutqn,q15);
  xoverschr:=xoverschrijding(fileoutqn,15);
  writeln(fileoutstat,'q15 ',format('%8.1f',[xoverschr]),format('%8.1f',[ave]),
          format('%8.1f',[min]),format('%8.1f',[max]),
          format('%8.1f',[sdev]),format('%8.1f',[svar]),
          format('%8.1f',[overschr]));
  q100array(fileoutqn,q100arr);
  statisticsshort(q100arr,narr,min,max,ave,adev,sdev,svar,skew,curt);
  q100:=ave;
  overschr:=overschrijding(fileoutqn,q100);
  xoverschr:=xoverschrijding(fileoutqn,100);
  writeln(fileoutstat,'q100',format('%8.1f',[xoverschr]),format('%8.1f',[ave]),
          format('%8.1f',[min]),format('%8.1f',[max]),
          format('%8.1f',[sdev]),format('%8.1f',[svar]),
          format('%8.1f',[overschr]));
  closefile(fileoutstat);

  writeln (fileoutall,format('%5.0d',[runnr]),format('%8.1f',[hgem]),
               format('%8.0f',[drainageweerstand]),
               format('%8.3f',[bergingscoefficient]),
               format('%8.1f',[qbot]),format('%8.4f',[delta]),
               format('%8.4f',[omega]),format('%8.1f',[cw]),
               format('%8.1f',[ghg]),format('%8.1f',[gvg]),
               format('%8.1f',[glg]),format('%8.1f',[xoverschrGLG]),
               format('%8.1f',[q1]));

   end;
  close(filein);
  close(fileoutall);
end;
{**************************************************************************}

//
//
// =================== Start Hoofdprogramma ====================================
//
//
Var
  fileinparamn,fileinmeteon,fileoutn: string;
  path: string;

  BEGIN
  // Check of het aantal parameters correct is ...
  if paramcount<>3 then begin
   writeln;
   writeln('Syntax: '+ExtractFileName(ParamStr(0))+' [bodem-_en_opdrachtparameters] [meteobestand] [prefix_output]');
   halt;
  end;

  logfile:='../'+ExtractFileName(ChangeFileExt(ParamStr(0),'.log'));

  // Pararameters toekennen aan variabelen..
  fileinparamn := ParamStr(1);
  fileinmeteon := ParamStr(2);
  outn := ParamStr(3);

  if not FileExists(fileinparamn) then begin
    writelog(fileinn, outn);
    halt;
  end;

  // grondwaterstand
  NLT(fileinparamn,fileinmeteon,outn,fileoutn,path);

end.








