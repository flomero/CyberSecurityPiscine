int _init(EVP_PKEY_CTX *ctx)
{
  int iVar1;
  
  iVar1 = __gmon_start__();
  return iVar1;
}

void FUN_00101020(void)
{
  (*(code *)(undefined *)0x0)();
  return;
}

int puts(char *__s)
{
  int iVar1;
  
  iVar1 = puts(__s);
  return iVar1;
}

size_t strlen(char *__s)

{
  size_t sVar1;
  
  sVar1 = strlen(__s);
  return sVar1;
}

int printf(char *__format,...)
{
  int iVar1;
  
  iVar1 = printf(__format);
  return iVar1;
}

void * memset(void *__s,int __c,size_t __n)
{
  void *pvVar1;
  
  pvVar1 = memset(__s,__c,__n);
  return pvVar1;
}

int strcmp(char *__s1,char *__s2)
{
  int iVar1;
  
  iVar1 = strcmp(__s1,__s2);
  return iVar1;
}

int fflush(FILE *__stream)

{
  int iVar1;
  iVar1 = fflush(__stream);
  return iVar1;
}

int atoi(char *__nptr)
{
  int iVar1;
  
  iVar1 = atoi(__nptr);
  return iVar1;
}

void __isoc99_scanf(void)
{
  __isoc99_scanf();
  return;
}

void exit(int __status)
{
  exit(__status);
}

void __cxa_finalize(void)
{
  __cxa_finalize();
  return;
}

void processEntry _start(undefined8 param_1,undefined8 param_2)
{
  undefined auStack_8 [8];
  
  __libc_start_main(main,param_2,&stack0x00000008,0,0,param_1,auStack_8);
  do {
                    // WARNING: Do nothing block with infinite loop
  } while( true );
}

void __do_global_dtors_aux(void)
{
  if (completed_0 != '\0') {
    return;
  }
  __cxa_finalize(__dso_handle);
  deregister_tm_clones();
  completed_0 = 1;
  return;
}

void wt(void)
{
  puts("********");
  return;
}

int nice(int __inc)
{
  int iVar1;
  
  iVar1 = puts("nice");
  return iVar1;
}

void try(void)
{
  puts("try");
  return;
}

void but(void)
{
  puts("but");
  return;
}

void this(void)
{
  puts("this");
  return;
}

void it(void)
{
  puts("it");
  return;
}

void not(void)
{
  puts("not.");
  return;
}

void that(void)
{
  puts("that.");
  return;
}

void easy(void)
{
  puts("easy.");
  return;
}

void ___syscall_malloc(void)
{
  puts("Nope.");
  exit(1);
}

void ____syscall_malloc(void)
{
  puts("Good job.");
  return;
}

int main(void)
{
  ulong uVar1;
  int iVar2;
  size_t sVar3;
  bool bVar4;
  char local_4c;
  char local_4b;
  char local_4a;
  undefined local_49;
  char local_48 [31];
  char local_29 [9];
  ulong local_20;
  int local_18;
  int local_14;
  int local_10;
  undefined4 local_c;
  
  local_c = 0;
  printf("Please enter key: ");
  local_10 = __isoc99_scanf(&DAT_00102056);
  if (local_10 != 1) {
    ___syscall_malloc();
  }
  if (local_48[1] != '2') {
    ___syscall_malloc();
  }
  if (local_48[0] != '4') {
    ___syscall_malloc();
  }
  fflush(_stdin);
  memset(local_29,0,9);
  local_29[0] = '*';
  local_49 = 0;
  local_20 = 2;
  local_14 = 1;
  while( true ) {
    sVar3 = strlen(local_29);
    uVar1 = local_20;
    bVar4 = false;
    if (sVar3 < 8) {
      sVar3 = strlen(local_48);
      bVar4 = uVar1 < sVar3;
    }
    if (!bVar4) break;
    local_4c = local_48[local_20];
    local_4b = local_48[local_20 + 1];
    local_4a = local_48[local_20 + 2];
    iVar2 = atoi(&local_4c);
    local_29[local_14] = (char)iVar2;
    local_20 = local_20 + 3;
    local_14 = local_14 + 1;
  }
  local_29[local_14] = '\0';
  local_18 = strcmp(local_29,"********");
  if (local_18 == -2) {
    ___syscall_malloc();
  }
  else if (local_18 == -1) {
    ___syscall_malloc();
  }
  else if (local_18 == 0) {
    ____syscall_malloc();
  }
  else if (local_18 == 1) {
    ___syscall_malloc();
  }
  else if (local_18 == 2) {
    ___syscall_malloc();
  }
  else if (local_18 == 3) {
    ___syscall_malloc();
  }
  else if (local_18 == 4) {
    ___syscall_malloc();
  }
  else if (local_18 == 5) {
    ___syscall_malloc();
  }
  else if (local_18 == 0x73) {
    ___syscall_malloc();
  }
  else {
    ___syscall_malloc();
  }
  return 0;
}