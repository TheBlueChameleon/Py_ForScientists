	.file	"main.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC1:
	.string	"naive:\n"
.LC5:
	.string	"got %lld in %f ms\n"
	.text
	.p2align 4
	.globl	naive
	.type	naive, @function
naive:
.LFB5495:
	.cfi_startproc
	endbr64
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	leaq	.LC1(%rip), %rsi
	xorl	%eax, %eax
	leaq	16(%rsp), %r13
	.cfi_def_cfa 13, 0
	andq	$-64, %rsp
	pushq	-8(%r13)
	pushq	%rbp
	movq	%rsp, %rbp
	.cfi_escape 0x10,0x6,0x2,0x76,0
	pushq	%r13
	.cfi_escape 0xf,0x3,0x76,0x78,0x6
	pushq	%r12
	pushq	%rbx
	.cfi_escape 0x10,0xc,0x2,0x76,0x70
	.cfi_escape 0x10,0x3,0x2,0x76,0x68
	movl	%edi, %ebx
	movl	$1, %edi
	subq	$24, %rsp
	call	__printf_chk@PLT
	call	clock@PLT
	movq	%rax, %r13
	testl	%ebx, %ebx
	jle	.L7
	leal	-1(%rbx), %eax
	cmpl	$14, %eax
	jbe	.L8
	movl	%ebx, %edx
	xorl	%eax, %eax
	vpxor	%xmm1, %xmm1, %xmm1
	vmovdqa32	.LC0(%rip), %zmm3
	vpbroadcastd	.LC6(%rip), %zmm4
	shrl	$4, %edx
	.p2align 4,,10
	.p2align 3
.L4:
	vmovdqa32	%zmm3, %zmm0
	addl	$1, %eax
	vpaddd	%zmm4, %zmm3, %zmm3
	vpmovsxdq	%ymm0, %zmm2
	vextracti64x4	$0x1, %zmm0, %ymm0
	vpaddq	%zmm1, %zmm2, %zmm1
	vpmovsxdq	%ymm0, %zmm0
	vpaddq	%zmm1, %zmm0, %zmm1
	cmpl	%eax, %edx
	jne	.L4
	vmovdqa	%ymm1, %ymm0
	vextracti64x4	$0x1, %zmm1, %ymm1
	movl	%ebx, %eax
	vpaddq	%ymm1, %ymm0, %ymm1
	andl	$-16, %eax
	vmovdqa	%xmm1, %xmm0
	vextracti128	$0x1, %ymm1, %xmm1
	vpaddq	%xmm1, %xmm0, %xmm0
	vpsrldq	$8, %xmm0, %xmm1
	vpaddq	%xmm1, %xmm0, %xmm0
	vmovq	%xmm0, %r12
	testb	$15, %bl
	je	.L13
	vzeroupper
.L3:
	movslq	%eax, %rdx
	addq	%rdx, %r12
	leal	1(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	2(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	3(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	4(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	5(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	6(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	7(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	8(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	9(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	10(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	11(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	12(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addq	%rdx, %r12
	leal	13(%rax), %edx
	cmpl	%edx, %ebx
	jle	.L2
	movslq	%edx, %rdx
	addl	$14, %eax
	addq	%rdx, %r12
	movslq	%eax, %rdx
	addq	%r12, %rdx
	cmpl	%eax, %ebx
	cmovg	%rdx, %r12
.L2:
	call	clock@PLT
	vxorps	%xmm0, %xmm0, %xmm0
	movq	%r12, %rdx
	movl	$1, %edi
	subq	%r13, %rax
	leaq	.LC5(%rip), %rsi
	vcvtsi2sdq	%rax, %xmm0, %xmm0
	vmulsd	.LC3(%rip), %xmm0, %xmm0
	movl	$1, %eax
	vdivsd	.LC4(%rip), %xmm0, %xmm0
	addq	$24, %rsp
	popq	%rbx
	popq	%r12
	popq	%r13
	.cfi_remember_state
	.cfi_def_cfa 13, 0
	popq	%rbp
	leaq	-16(%r13), %rsp
	.cfi_def_cfa 7, 16
	popq	%r13
	.cfi_def_cfa_offset 8
	jmp	__printf_chk@PLT
	.p2align 4,,10
	.p2align 3
.L7:
	.cfi_restore_state
	xorl	%r12d, %r12d
	jmp	.L2
.L8:
	xorl	%eax, %eax
	xorl	%r12d, %r12d
	jmp	.L3
.L13:
	vzeroupper
	jmp	.L2
	.cfi_endproc
.LFE5495:
	.size	naive, .-naive
	.section	.rodata.str1.1
.LC7:
	.string	"intrinsics:\n"
	.text
	.p2align 4
	.globl	intrinsics
	.type	intrinsics, @function
intrinsics:
.LFB5496:
	.cfi_startproc
	endbr64
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	leaq	.LC7(%rip), %rsi
	xorl	%eax, %eax
	leaq	16(%rsp), %r13
	.cfi_def_cfa 13, 0
	andq	$-64, %rsp
	pushq	-8(%r13)
	pushq	%rbp
	movq	%rsp, %rbp
	.cfi_escape 0x10,0x6,0x2,0x76,0
	pushq	%r13
	.cfi_escape 0xf,0x3,0x76,0x78,0x6
	pushq	%r12
	pushq	%rbx
	.cfi_escape 0x10,0xc,0x2,0x76,0x70
	.cfi_escape 0x10,0x3,0x2,0x76,0x68
	movl	%edi, %ebx
	movl	$1, %edi
	subq	$88, %rsp
	call	__printf_chk@PLT
	call	clock@PLT
	movq	%rax, %r12
	testl	%ebx, %ebx
	jle	.L17
	movl	$1, %ecx
	movl	$8, %edi
	movl	$32, %esi
	xorl	%eax, %eax
	kmovw	%ecx, %k0
	movl	$2, %ecx
	kmovw	%edi, %k5
	kmovw	%esi, %k3
	vpxor	%xmm1, %xmm1, %xmm1
	kmovw	%ecx, %k7
	movl	$4, %ecx
	movl	$64, %edi
	kmovw	%ecx, %k6
	vmovdqa64	%zmm1, %zmm0
	movl	$16, %ecx
	kmovw	%edi, %k2
	movl	$-128, %esi
	kmovw	%ecx, %k4
	.p2align 4,,10
	.p2align 3
.L16:
	leaq	1(%rax), %rdx
	kmovw	%k0, %k1
	vpbroadcastq	%rax, %zmm0{%k1}
	kmovw	%esi, %k1
	vpbroadcastq	%rdx, %zmm0{%k7}
	leaq	2(%rax), %rdx
	vpbroadcastq	%rdx, %zmm0{%k6}
	leaq	3(%rax), %rdx
	vpbroadcastq	%rdx, %zmm0{%k5}
	leaq	4(%rax), %rdx
	vpbroadcastq	%rdx, %zmm0{%k4}
	leaq	5(%rax), %rdx
	vpbroadcastq	%rdx, %zmm0{%k3}
	leaq	6(%rax), %rdx
	vpbroadcastq	%rdx, %zmm0{%k2}
	leaq	7(%rax), %rdx
	addq	$8, %rax
	vpbroadcastq	%rdx, %zmm0{%k1}
	vpaddq	%zmm0, %zmm1, %zmm1
	cmpl	%eax, %ebx
	jg	.L16
.L15:
	vextracti64x4	$0x1, %zmm1, %ymm0
	vpaddq	%ymm1, %ymm0, %ymm0
	vextracti128	$0x1, %ymm0, %xmm1
	vpaddq	%xmm0, %xmm1, %xmm1
	vmovdqa	%xmm1, -64(%rbp)
	vzeroupper
	call	clock@PLT
	vxorps	%xmm0, %xmm0, %xmm0
	movl	$1, %edi
	vmovdqa	-64(%rbp), %xmm1
	subq	%r12, %rax
	leaq	.LC5(%rip), %rsi
	vcvtsi2sdq	%rax, %xmm0, %xmm0
	vpsrldq	$8, %xmm1, %xmm2
	movl	$1, %eax
	vmulsd	.LC3(%rip), %xmm0, %xmm0
	vpaddq	%xmm2, %xmm1, %xmm1
	vdivsd	.LC4(%rip), %xmm0, %xmm0
	addq	$88, %rsp
	vmovq	%xmm1, %rdx
	popq	%rbx
	popq	%r12
	popq	%r13
	.cfi_remember_state
	.cfi_def_cfa 13, 0
	popq	%rbp
	leaq	-16(%r13), %rsp
	.cfi_def_cfa 7, 16
	popq	%r13
	.cfi_def_cfa_offset 8
	jmp	__printf_chk@PLT
.L17:
	.cfi_restore_state
	vpxor	%xmm1, %xmm1, %xmm1
	jmp	.L15
	.cfi_endproc
.LFE5496:
	.size	intrinsics, .-intrinsics
	.section	.rodata.str1.1
.LC9:
	.string	"intrinsics improved:\n"
	.text
	.p2align 4
	.globl	intrinsics_improved
	.type	intrinsics_improved, @function
intrinsics_improved:
.LFB5497:
	.cfi_startproc
	endbr64
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	leaq	.LC9(%rip), %rsi
	xorl	%eax, %eax
	leaq	16(%rsp), %r13
	.cfi_def_cfa 13, 0
	andq	$-64, %rsp
	pushq	-8(%r13)
	pushq	%rbp
	movq	%rsp, %rbp
	.cfi_escape 0x10,0x6,0x2,0x76,0
	pushq	%r13
	.cfi_escape 0xf,0x3,0x76,0x78,0x6
	pushq	%r12
	pushq	%rbx
	.cfi_escape 0x10,0xc,0x2,0x76,0x70
	.cfi_escape 0x10,0x3,0x2,0x76,0x68
	movl	%edi, %ebx
	movl	$1, %edi
	subq	$88, %rsp
	call	__printf_chk@PLT
	call	clock@PLT
	vpxor	%xmm1, %xmm1, %xmm1
	movq	%rax, %r12
	testl	%ebx, %ebx
	jle	.L21
	vmovdqa64	.LC8(%rip), %zmm0
	xorl	%edx, %edx
	vpbroadcastq	.LC11(%rip), %zmm2
	.p2align 4,,10
	.p2align 3
.L22:
	addl	$8, %edx
	vpaddq	%zmm0, %zmm1, %zmm1
	vpaddq	%zmm2, %zmm0, %zmm0
	cmpl	%edx, %ebx
	jg	.L22
.L21:
	vextracti64x4	$0x1, %zmm1, %ymm0
	vpaddq	%ymm1, %ymm0, %ymm0
	vextracti128	$0x1, %ymm0, %xmm1
	vpaddq	%xmm0, %xmm1, %xmm1
	vmovdqa	%xmm1, -64(%rbp)
	vzeroupper
	call	clock@PLT
	vxorps	%xmm0, %xmm0, %xmm0
	movl	$1, %edi
	vmovdqa	-64(%rbp), %xmm1
	subq	%r12, %rax
	leaq	.LC5(%rip), %rsi
	vcvtsi2sdq	%rax, %xmm0, %xmm0
	vpsrldq	$8, %xmm1, %xmm2
	movl	$1, %eax
	vmulsd	.LC3(%rip), %xmm0, %xmm0
	vpaddq	%xmm2, %xmm1, %xmm1
	vdivsd	.LC4(%rip), %xmm0, %xmm0
	addq	$88, %rsp
	vmovq	%xmm1, %rdx
	popq	%rbx
	popq	%r12
	popq	%r13
	.cfi_def_cfa 13, 0
	popq	%rbp
	leaq	-16(%r13), %rsp
	.cfi_def_cfa 7, 16
	popq	%r13
	.cfi_def_cfa_offset 8
	jmp	__printf_chk@PLT
	.cfi_endproc
.LFE5497:
	.size	intrinsics_improved, .-intrinsics_improved
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB5498:
	.cfi_startproc
	endbr64
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$1000000, %edi
	call	naive
	movl	$1000000, %edi
	call	intrinsics
	movl	$1000000, %edi
	call	intrinsics_improved
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE5498:
	.size	main, .-main
	.section	.rodata
	.align 64
.LC0:
	.long	0
	.long	1
	.long	2
	.long	3
	.long	4
	.long	5
	.long	6
	.long	7
	.long	8
	.long	9
	.long	10
	.long	11
	.long	12
	.long	13
	.long	14
	.long	15
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC3:
	.long	0
	.long	1083129856
	.align 8
.LC4:
	.long	0
	.long	1093567616
	.section	.rodata.cst4,"aM",@progbits,4
	.align 4
.LC6:
	.long	16
	.section	.rodata
	.align 64
.LC8:
	.quad	0
	.quad	1
	.quad	2
	.quad	3
	.quad	4
	.quad	5
	.quad	6
	.quad	7
	.section	.rodata.cst8
	.align 8
.LC11:
	.quad	8
	.ident	"GCC: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
