
subrutina escribir_simbolo(s) { alfabeto {1,_} estados{qE,qF} inicial:qE; finales:{qF}; transiciones{qE,_->qF,s,DER; qE,1->qF,s,DER;} }
subrutina escribir_unos(n) { alfabeto {1,_} estados{ini,fin} inicial:ini; finales:{fin}; usa escribir_simbolo(1) repetir n como e; transiciones{ ini,_->e_ini,_,QUIETO; ini,1->e_ini,1,QUIETO; e_fin,_->fin,_,QUIETO; e_fin,1->fin,1,QUIETO;} }
maquina M1 { alfabeto {1,_} estados{i,f} inicial:i; finales:{f}; usa escribir_unos(1) como a; transiciones{ i,_->a_ini,_,QUIETO; a_fin,_->f,_,QUIETO;} }
maquina M5 { alfabeto {1,_} estados{i,f} inicial:i; finales:{f}; usa escribir_unos(5) como a; transiciones{ i,_->a_ini,_,QUIETO; a_fin,_->f,_,QUIETO;} }
maquina M23 { alfabeto {1,_} estados{i,f} inicial:i; finales:{f}; usa escribir_unos(2) como a; usa escribir_unos(3) como b; transiciones{ i,_->a_ini,_,QUIETO; a_fin,_->b_ini,_,QUIETO; b_fin,_->f,_,QUIETO; } }
