# bmstu_stend_pc

программа для обчного пк 

ждет подключения по адресам "127.0.0.1":9000 - модель  "127.0.0.1" 9010 - борт

модель в ответ на 'M' высылает следующие структуры подряд:

struct Model_i
{
    double M_o_Omg[3]; //угловые скорости модели
    double o_Omg[3]; // угловые скорости с дус
    double i_Moment[3]; // моменты
    double o_Quat[4]; // кватернион
    double S_i[3]; // вектор Солнца в ИСК
    double S_cck[3]; // вектор Солнца в ССК
    unsigned short Sn; // Наличие Солнца

    unsigned short o_P[8]; // Признаки включения двигателей

};
struct sim_time_t { // время от старта модели
    unsigned char Hour; // часы
    unsigned char Minute; // минут
    unsigned char Second; // секунды
    unsigned short Mls;	// миллисекунды
};

борт в ответ на 'S' высылает следующие структуры подряд:

struct Pso_i /* Структура для переменных режима ПСО (построения солнечной ориентации) */
{
    double o_Omg[3]; //угловый скорости
    double S_cck[3]; //направляющие косинусы на солнце в сск
    double u_wPro[3]; /* вектор программной скорости */
    unsigned short o_P[8]; /* Признаки включения двигателей на текущем шаге */
    unsigned short Sn; // признак наличия солнца
    double u_Kp;             //= 1; коэффициент пропорционального звена
    double u_Ki;             //= 0; коэффициент интегрирующего звена
    double u_Kd;             //коэффициент дифференцирующего звена

    double o_wCurrent[3]; /* текущая скорость */
    double i_sigma[3]; /* аргумент управления */
    double n_wStab[3];
    double u_wInitial[3]; /* начальная скорость */
};

struct sim_time_t { // время от старта борта
    unsigned char Hour; // часы
    unsigned char Minute; // минут
    unsigned char Second; // секунды
    unsigned short Mls;	// миллисекунды
};
