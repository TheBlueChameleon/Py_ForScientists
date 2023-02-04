	.file	"main.c"
	.text
	.section	.rodata
.LC0:
	.string	"naive:"
.LC3:
	.string	"got %lld in %f ms\n"
	.text
	.globl	naive
	.type	naive, @function
naive:
.LFB4197:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$64, %rsp
	movl	%edi, -52(%rbp)
	leaq	.LC0(%rip), %rax
	movq	%rax, %rdi
	call	puts@PLT
	call	clock@PLT
	movq	%rax, -24(%rbp)
	movq	$0, -32(%rbp)
	movl	$0, -36(%rbp)
	jmp	.L2
.L3:
	movl	-36(%rbp), %eax
	cltq
	addq	%rax, -32(%rbp)
	addl	$1, -36(%rbp)
.L2:
	movl	-36(%rbp), %eax
	cmpl	-52(%rbp), %eax
	jl	.L3
	call	clock@PLT
	movq	%rax, -16(%rbp)
	movq	-16(%rbp), %rax
	subq	-24(%rbp), %rax
	vcvtsi2sdq	%rax, %xmm1, %xmm1
	vmovsd	.LC1(%rip), %xmm0
	vmulsd	%xmm0, %xmm1, %xmm0
	vmovsd	.LC2(%rip), %xmm1
	vdivsd	%xmm1, %xmm0, %xmm0
	vmovsd	%xmm0, -8(%rbp)
	movq	-8(%rbp), %rdx
	movq	-32(%rbp), %rax
	vmovq	%rdx, %xmm0
	movq	%rax, %rsi
	leaq	.LC3(%rip), %rax
	movq	%rax, %rdi
	movl	$1, %eax
	call	printf@PLT
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE4197:
	.size	naive, .-naive
	.section	.rodata
.LC4:
	.string	"intrinsics:"
	.text
	.globl	intrinsics
	.type	intrinsics, @function
intrinsics:
.LFB4198:
	.cfi_startproc
	endbr64
	leaq	8(%rsp), %r10
	.cfi_def_cfa 10, 0
	andq	$-64, %rsp
	pushq	-8(%r10)
	pushq	%rbp
	movq	%rsp, %rbp
	.cfi_escape 0x10,0x6,0x2,0x76,0
	pushq	%r10
	.cfi_escape 0xf,0x3,0x76,0x78,0x6
	subq	$424, %rsp
	movl	%edi, -420(%rbp)
	movq	%fs:40, %rax
	movq	%rax, -56(%rbp)
	xorl	%eax, %eax
	leaq	.LC4(%rip), %rax
	movq	%rax, %rdi
	call	puts@PLT
	call	clock@PLT
	movq	%rax, -392(%rbp)
	vpxor	%xmm0, %xmm0, %xmm0
	vmovdqa64	%zmm0, -368(%rbp)
	vpxor	%xmm0, %xmm0, %xmm0
	vmovdqa64	%zmm0, -304(%rbp)
	movq	$0, -400(%rbp)
	movl	$0, -412(%rbp)
	jmp	.L5
.L9:
	movl	$0, -408(%rbp)
	jmp	.L6
.L7:
	movl	-412(%rbp), %edx
	movl	-408(%rbp), %eax
	addl	%edx, %eax
	movslq	%eax, %rdx
	movl	-408(%rbp), %eax
	cltq
	movq	%rdx, -304(%rbp,%rax,8)
	addl	$1, -408(%rbp)
.L6:
	cmpl	$7, -408(%rbp)
	jle	.L7
	vmovdqa64	-304(%rbp), %zmm0
	vmovdqa64	-368(%rbp), %zmm1
	vmovdqa64	%zmm1, -240(%rbp)
	vmovdqa64	%zmm0, -176(%rbp)
	vmovdqa64	-240(%rbp), %zmm1
	vmovdqa64	-176(%rbp), %zmm0
	vpaddq	%zmm0, %zmm1, %zmm0
	nop
	vmovdqa64	%zmm0, -368(%rbp)
	addl	$8, -412(%rbp)
.L5:
	movl	-412(%rbp), %eax
	cmpl	-420(%rbp), %eax
	jl	.L9
	movl	$0, -404(%rbp)
	jmp	.L10
.L11:
	movl	-404(%rbp), %eax
	cltq
	movq	-368(%rbp,%rax,8), %rax
	addq	%rax, -400(%rbp)
	addl	$1, -404(%rbp)
.L10:
	cmpl	$7, -404(%rbp)
	jle	.L11
	call	clock@PLT
	movq	%rax, -384(%rbp)
	movq	-384(%rbp), %rax
	subq	-392(%rbp), %rax
	vcvtsi2sdq	%rax, %xmm1, %xmm1
	vmovsd	.LC1(%rip), %xmm0
	vmulsd	%xmm0, %xmm1, %xmm0
	vmovsd	.LC2(%rip), %xmm1
	vdivsd	%xmm1, %xmm0, %xmm0
	vmovsd	%xmm0, -376(%rbp)
	movq	-376(%rbp), %rdx
	movq	-400(%rbp), %rax
	vmovq	%rdx, %xmm0
	movq	%rax, %rsi
	leaq	.LC3(%rip), %rax
	movq	%rax, %rdi
	movl	$1, %eax
	call	printf@PLT
	nop
	movq	-56(%rbp), %rax
	subq	%fs:40, %rax
	je	.L12
	call	__stack_chk_fail@PLT
.L12:
	movq	-8(%rbp), %r10
	.cfi_def_cfa 10, 0
	leave
	leaq	-8(%r10), %rsp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE4198:
	.size	intrinsics, .-intrinsics
	.section	.rodata
.LC5:
	.string	"intrinsics improved:"
	.text
	.globl	intrinsics_improved
	.type	intrinsics_improved, @function
intrinsics_improved:
.LFB4199:
	.cfi_startproc
	endbr64
	leaq	8(%rsp), %r10
	.cfi_def_cfa 10, 0
	andq	$-64, %rsp
	pushq	-8(%r10)
	pushq	%rbp
	movq	%rsp, %rbp
	.cfi_escape 0x10,0x6,0x2,0x76,0
	pushq	%r10
	.cfi_escape 0xf,0x3,0x76,0x78,0x6
	subq	$616, %rsp
	movl	%edi, -612(%rbp)
	movq	%fs:40, %rax
	movq	%rax, -56(%rbp)
	xorl	%eax, %eax
	leaq	.LC5(%rip), %rax
	movq	%rax, %rdi
	call	puts@PLT
	call	clock@PLT
	movq	%rax, -584(%rbp)
	vpxor	%xmm0, %xmm0, %xmm0
	vmovdqa64	%zmm0, -560(%rbp)
	vmovdqa64	.LC6(%rip), %zmm0
	vmovdqa64	%zmm0, -496(%rbp)
	vpbroadcastq	.LC8(%rip), %zmm0
	vmovdqa64	%zmm0, -432(%rbp)
	movq	$0, -592(%rbp)
	movl	$0, -600(%rbp)
	jmp	.L14
.L17:
	vmovdqa64	-560(%rbp), %zmm0
	vmovdqa64	%zmm0, -240(%rbp)
	vmovdqa64	-496(%rbp), %zmm0
	vmovdqa64	%zmm0, -176(%rbp)
	vmovdqa64	-240(%rbp), %zmm1
	vmovdqa64	-176(%rbp), %zmm0
	vpaddq	%zmm0, %zmm1, %zmm0
	vmovdqa64	%zmm0, -560(%rbp)
	vmovdqa64	-496(%rbp), %zmm0
	vmovdqa64	%zmm0, -368(%rbp)
	vmovdqa64	-432(%rbp), %zmm0
	vmovdqa64	%zmm0, -304(%rbp)
	vmovdqa64	-368(%rbp), %zmm1
	vmovdqa64	-304(%rbp), %zmm0
	vpaddq	%zmm0, %zmm1, %zmm0
	nop
	vmovdqa64	%zmm0, -496(%rbp)
	addl	$8, -600(%rbp)
.L14:
	movl	-600(%rbp), %eax
	cmpl	-612(%rbp), %eax
	jl	.L17
	movl	$0, -596(%rbp)
	jmp	.L18
.L19:
	movl	-596(%rbp), %eax
	cltq
	movq	-560(%rbp,%rax,8), %rax
	addq	%rax, -592(%rbp)
	addl	$1, -596(%rbp)
.L18:
	cmpl	$7, -596(%rbp)
	jle	.L19
	call	clock@PLT
	movq	%rax, -576(%rbp)
	movq	-576(%rbp), %rax
	subq	-584(%rbp), %rax
	vcvtsi2sdq	%rax, %xmm1, %xmm1
	vmovsd	.LC1(%rip), %xmm0
	vmulsd	%xmm0, %xmm1, %xmm0
	vmovsd	.LC2(%rip), %xmm1
	vdivsd	%xmm1, %xmm0, %xmm0
	vmovsd	%xmm0, -568(%rbp)
	movq	-568(%rbp), %rdx
	movq	-592(%rbp), %rax
	vmovq	%rdx, %xmm0
	movq	%rax, %rsi
	leaq	.LC3(%rip), %rax
	movq	%rax, %rdi
	movl	$1, %eax
	call	printf@PLT
	nop
	movq	-56(%rbp), %rax
	subq	%fs:40, %rax
	je	.L20
	call	__stack_chk_fail@PLT
.L20:
	movq	-8(%rbp), %r10
	.cfi_def_cfa 10, 0
	leave
	leaq	-8(%r10), %rsp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE4199:
	.size	intrinsics_improved, .-intrinsics_improved
	.section	.rodata
.LC9:
	.string	"hello world"
.LC10:
	.string	"%lu\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB4200:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	andq	$-64, %rsp
	subq	$192, %rsp
	movq	%fs:40, %rax
	movq	%rax, 184(%rsp)
	xorl	%eax, %eax
	movl	$1000000, 60(%rsp)
	leaq	.LC9(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	prinf@PLT
	movl	$64, %esi
	leaq	.LC10(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$8, %esi
	leaq	.LC10(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	60(%rsp), %eax
	movl	%eax, %edi
	call	naive
	movl	60(%rsp), %eax
	movl	%eax, %edi
	call	intrinsics
	movl	60(%rsp), %eax
	movl	%eax, %edi
	call	intrinsics_improved
	movl	$0, %eax
	movq	184(%rsp), %rdx
	subq	%fs:40, %rdx
	je	.L23
	call	__stack_chk_fail@PLT
.L23:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE4200:
	.size	main, .-main
	.section	.rodata
	.align 8
.LC1:
	.long	0
	.long	1083129856
	.align 8
.LC2:
	.long	0
	.long	1093567616
	.align 64
.LC6:
	.quad	0
	.quad	1
	.quad	2
	.quad	3
	.quad	4
	.quad	5
	.quad	6
	.quad	7
	.align 8
.LC8:
	.quad	8
	.ident	"GCC: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0"
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
