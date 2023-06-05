typedef struct {
    double x;
    double y;
} point2d_t;

void func_void_empty();
void func_void_int(int);
void func_void_charPtr(char*);
void func_void_doublePtr(const double*);
void func_void_struct(point2d_t);
void func_void_structPtr(point2d_t*);

int func_int_empty();
const char* func_charPtr_empty();

// this is how you share global variables across modules in C
extern const double pi;
