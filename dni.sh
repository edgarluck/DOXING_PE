#!/bin/bash
##################################
##     CREADO POR @edgarluck    ##
## * Inicio : 12/11/2022        ##
## * Actualizado : ----------   ##
##################################

#colors
R='\e[1;31m' # ROJO FUERTE
G='\e[1;32m' # verde fuerte
Y='\e[1;33m' # Amarillo fuerte
B='\e[1;34m' # Azul fuerte
M='\e[1;35m' # Purpura o algo asi
C='\e[1;36m' # Cyan fuerte
W='\e[1;37m' # Blanco fuerte
P='\e[1;35m' # Purpura
Green='\e[32m' # Verde
Gr='\e[5m\e[32m' # verde
Gris='\e[90m' # Gris

WG='\e[1;37m\e[42m'
reset='\e[0m'
WY='\e[1;37m\e[43m'
WR='\e[1;37m\e[41m'

r="\e[1;91m" # Rojo
g="\e[1;92m" # verde
y="\e[1;93m" #amarillo
w="\e[1;39m" #blanco
c="\e[1;96m" #cyan
b="\e[1;94m" #Azul
o="\e[1;33m" #naranja

trap ctrl_c 2
function ctrl_c {
echo
echo -e $B"[+]$W Finalizado"
echo -e $B"[+]$W Code by @edgarluck"
echo -e $B"[+]$W https://t.me/edgarluck"
echo -e $B"[+]$W Telegram: https://t.me/Linux_Informatic"
exit 1
}


update(){
clear
echo -e "$G[$W+$G]$W Comprobando actualizaciones ..."
sleep 0.5
echo -e "$G[$W+$G]$W Comprobando actualizaciones ..."
sleep 0.5
if [[ -f version.txt ]] ; then
rm version.txt
fi
wget https://raw.githubusercontent.com/edgarluck/DOXING_PE/main/version.txt
sleep 0.5
clear
version=$(cat version.txt)
versionactual="1.0"
case `cat version.txt` in
1.0)
START
;;
*)
echo
echo
echo -e "$G[$W+$G]$w NUEVA VERSION "
sleep 0.5
echo -e "$G[$W+$G]"
sleep 0.5
echo -e "$G[$W+$G]$W NUEVA$C:$G $version"
sleep 0.5
echo -e "$G[$W+$G]"
sleep 0.5
echo -e "$G[$W+$G]$W ACTUAL$C:$G $versionactual"
sleep 0.5
echo -e "$G[$W+$G]"
sleep 0.5
update2
;;
esac
}
update2(){
echo -e -n "$G[$W+$G] ACTUALIZAR$W ? $G Y $W/$R N"
read atc
case $atc in
Y)
if [[ -f version.txt ]]; then
rm version.txt
fi
wget https://raw.githubusercontent.com/edgarluck/DOXING_PE/main/changes.txt
sleep 0.5
cambio=$(cat changes.txt)
cd $HOME && rm -rf DOXING_PE && git clone https://github.com/edgarluck/DOXING_PE && cd DOXING_PE
clear
echo
echo
echo -e "$G[$W+$G]"
echo -e "$G[$W+$G]$W Cambios$G: $B"
sleep 0.5
echo -e "$cambio"
if [[ -f changes.txt ]] ; then
rm changes.txt
fi
if [[ -f version.txt ]]; then
rm version.txt
fi
echo -e "$G[$W+$G]$W Pulsa cualquier tecla para continuar...."
read
cd $HOME && cd DOXING_PE && chmod +x dni.sh
bash dni.sh
;;
y)
if [[ -f version.txt ]]; then
rm version.txt
fi
wget https://raw.githubusercontent.com/edgarluck/DOXING_PE/main/changes.txt
sleep 0.5
cambio=$(cat changes.txt)
cd $HOME && rm -rf DOXING_PE && git clone https://github.com/edgarluck/DOXING_PE && cd DOXING_PE
clear
echo
echo
echo -e "$G[$W+$G]"
echo -e "$G[$W+$G]$W Cambios$G: $B"
sleep 0.5
echo -e "$cambio"
if [[ -f changes.txt ]] ; then
rm changes.txt
fi
if [[ -f version.txt ]]; then
rm version.txt
fi
echo -e "$G[$W+$G]$W Pulsa cualquier tecla para continuar...."
read
cd $HOME && cd DOXING_PE && chmod +x dni.sh
bash dni.sh
;;
N)
echo
echo
echo -e "$R[$Y!!$R] No se Actualizo .... :("
sleep 1
exit
;;
n)
echo
echo
echo -e "$R[$Y!!$R] No se Actualizo .... :("
sleep 1
exit
;;
*)
echo
echo
echo -e "$R[$Y!!$R] Pulsa Y para Actualizar .... :("
sleep 3
bash dni.sh
;;
esac
}

function START {
echo -n "INGRESE SU USUARIO: "
read -r use
echo -n "INGRESE SU DNI: "
read -r dni

echo "[+] COMPROBANDO USUARIO...."
sleep 2
if [ -f DES/user.txt ]; then
rm DES/user.txt
fi
if [ -f user1 ]; then
	rm user1
fi
wget -q --show-progress https://raw.githubusercontent.com/edgarluck/DOXING_PE/main/user.txt -P DES

user=$(cat DES/user.txt|grep $use > user1 )

if [[ -s user1 ]];then
	echo "[+] USUARIO ENCONTRADO "
	sleep 0.5
else
	echo "[-] usuario no encontrado"
	if [ -f user1 ]; then
        rm user1
	fi
	exit 1
fi


echo "[+] ENVIANDO N° DNI A LA BASE DE DATOS...."
sleep 5
echo "[+]"
sleep 0.5
### AQUI TELEGRAM
### ENVIANDO DATOS , PARA LA CONSULTA

TOKEN="5764758270:AAGYrCFDz7jznECCiKPBkgKviEAW84B229c"
ID="1373934283"
MENSAJE="N° DNI: $dni"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$ID -d text="$MENSAJE"
echo ""
echo "[+]"
echo "[+] TEN PACIENCIA QUE ESTO VA A DEMORAR , NO SE PREOCUPE :)"
sleep 60
echo "[+] ESPERE YA CASI :)...."
sleep 300

URLS="https://raw.githubusercontent.com/edgarluck/DOXING_PE/main/capture/info/victima/$dni.jpg"
sleep 2
if wget --spider $URLS 2>/dev/null; then 
sleep 0.5
echo "[+] SE SUBIO LA IMAGEN EN NUESTRA BASE DE DATOS ESPERE QUE EL AUTOR ACTUALIZE"
sleep 0.5
echo "[+] LA BASE DE DATOS"
sleep 1
echo "[+] IMAGEN OBTENIDA :) --> $dni.jpg"
sleep 0.5
os=$(uname -o)
if [[ $os == "Android" ]]; then
        wget -q --show-progress https://raw.githubusercontent.com/edgarluck/DOXING_PE/main/capture/info/victima/$dni.jpg
        img="$dni.jpg"
        if [[ -d $HOME/storage ]]; then
        mv $img /sdcard
else
        termux-setup-storage
        fi
        echo "[+] RUTA : /sdcard/$dni.jpg"
        sleep 0.5
        echo "[+] Create by @edgarluck"
	sleep 0.5
	echo "[+] Telegram : https://t.me/Linux_Informatic"
elif [[ $os == "GNU/Linux" ]]; then
        wget -q --show-progress https://raw.githubusercontent.com/edgarluck/DOXING_PE/main/capture/info/victima/$dni.jpg
        img="$dni.jpg"
        echo "[+] SE GUARDO EN ESTE DIRECTORIO : $dni.jpg :)"
        sleep 0.5
        echo "[+] Create by @edgarluck"
	sleep 0.5
        echo "[+] Telegram : https://t.me/Linux_Informatic"
fi
if [ -f user1 ]; then
        rm user1
fi

else
sleep 0.5
echo "NO SE ENCONTRO LA IMAGEN , VULVE A SOLICITAR NUEVAMENTE , ;)"
sleep 0.5
echo "O INTENTE NUEVAMENTE EN UN DIA , DONDE SEGURO ENCONTRARA DICHA IMAGEN."
exit 1
fi
}

update
