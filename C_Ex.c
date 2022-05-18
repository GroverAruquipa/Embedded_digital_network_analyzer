// MUtex sincronizar variable compartida por varios hilos
// Ejemplo proteccion de una variable global

#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>
#include <stdio.h>


static int count=0; // Resorces shared
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
int pthread_mutex_lock(pthread_mutex_t *mutex);
int pthread_mutex_unlock(pthread_mutex_t *mutex);

// Semaforos son mecanismos de sincronizacion
// Protegen acceso a una seccion critica
static *void thread1_function(void *arg);
static *void thread2_function(void *arg);

int main(void){
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, *thread1_function, NULL);
    pthread_create(&thread2, NULL, *thread2_function, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("count = %d\n", count);
    return 0;

}
static void *thread1_function(void *arg){
    int i;
    for(i=0; i<10; i++){
        count=count+1;
        pthread_mutex_lock(&mutex);
        printf("Thread 1: %d\n", i);
        pthread_mutex_unlock(&mutex);
        sleep(1);
    }
}
static void *thread2_function(void *arg){
    int i;
    for(i=0; i<10; i--){
        count=count-1;
        pthread_mutex_lock(&mutex);
        printf("Thread 2: %d\n", i);
        pthread_mutex_unlock(&mutex);
        sleep(1);
    }
}


