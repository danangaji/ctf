[ID]

Saat awal menyelesaikan persoalan ini, kami menyelesaikan dengan menggunakan fungsi fibonacci yang sudah ada. Pada saat dijalankan iterasi 1 - 90 berjalan baik-baik saja karena N yang diminta masih dibawah N = 30. Sedangkan saat mencapai iterasi 91, nilai N yang diminta > 400 sehingga akan memakan banyak memori. Hal ini membuat waktu proses naik lebih dari yang diminta yaitu 25 detik.
Hingga kami mendapat sebuah deret angka yang menarik untuk masing-masing iterasi tial N yang diberikan yaitu:
```
0 - 1
1 - 1
2 - 2
3 - 4
4 - 8
5 - 14
6 - 24
7 - 40
```
Pola yang didapat adalah 
```
    |N < 2  ->  1
if -|N = 2  ->  2
    |N > 2  ->  sumiteration(N) = sumiteration(N-1) + sumiteration(N-2) + 2
```
Menjadi sebuah fungsi yang sederhana bukan?

Ketika [program](https://github.com/danangaji/ctf/blob/master/201612/3DS/PROG-400%20Fibonacci/fibo_prog.py) dijalankan pada iterasi ke 101 akan didapat flag yaitu:

> 3DS{g00d4lgorithmsC4nSaveYourTime}

