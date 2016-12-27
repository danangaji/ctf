# MISC-100 Santa Walk Into A Bar

```
[EN]
Santa walks into a bar and creates a friendship bound with you.
After some shots, he spells to you his secrets to delivery all gifts on Christmas: he has a magical linked list that inform the next kiddie to visit.
At the end of the night, he goes alway and left behind his wallet and the bag with the list of gifts to delivery. Try to discover if you will receive something.

[PT-BR]
Papai noel entra em um bar e cria um laço de amizade com voce.
Apos algumas bebidas, ele conta seu segredo para entregar todos os presentes de Natal: ele tem uma lista ligada que informa qual a porxima crianca que ele deve visitar. No final da noite,
ele foi embora e esqueceu a carteira e a bolsa com a lista de presentes para entregar. Tente descobrir se voce ira receber alguma coisa.
```

There are 11000 image of qr code we need to decode.
Simply loop in directory and run the zbarimg command
```
for i in $(ls);do zbarimg $i >> decode.txt;done
```
And then use awk to search something odd word

```
awk '{print $1}' decode.txt | sort | uniq
```

Tadaa.... 
```
QR-Code:A child
QR-Code:A kid
QR-Code:Fail 
QR-Code:I almost
QR-Code:Next kiddie
QR-Code:Next name
QR-Code:Now I
QR-Code:Ops! 
QR-Code:So wrong!
QR-Code:Wrong! 
QR-Code:Y0ur gift
QR-Code:Yu u
```

I think, we need to know what our gift.
```
grep 'Y0ur gift' decode.txt
```

It showing us the link

```
QR-Code:Y0ur gift is in goo.gl/wFGwqO inugky3leb2gqzjanruw42yk
```

And then follow the link to get the flag

3DS{I_h0p3_th4t_Y0u_d1d_n0t_h4v3_ch4ck3d_OnE_by_0n3}
