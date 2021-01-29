Lmain:

L1:	addi $sp,$sp,52
   	move $s0,$sp

L2:   	lw $t1,-12($sp)
   	li $t2,4
   	mul $t1,$t1,$t2
   	lw $t1,-24($sp)

L3:   	lw $t1,-16($sp)
   	lw $t2,-12($sp)
   	add $t1,$t1,$t2
   	lw $t1,-28($sp)

L4:   	li $t1,10
   	lw $t2,-28($sp)
   	div $t1,$t1,$t2
   	lw $t1,-32($sp)

L5:   	lw $t1,-28($sp)
   	lw $t2,-32($sp)
   	sub $t1,$t1,$t2
   	lw $t1,-36($sp)

L6:   	lw $t1,-36($sp)
   	sw $t1,-20($sp)

L7:   	lw $t1,-20($sp)
   	li $t2,7
   	add $t1,$t1,$t2
   	lw $t1,-40($sp)

L8:   	li $t1,2
   	lw $t2,-40($sp)
   	mul $t1,$t1,$t2
   	lw $t1,-44($sp)

L9:   	lw $t1,-44($sp)
   	li $v0,1
   	move $a0, $t1
   	syscall

L10:

L11:
