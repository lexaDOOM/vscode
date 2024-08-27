public class ShellSort {
    // Метод для сортировки массива
    public static void shellSort(int[] array) {
        int n = array.length;
        
        // Начальный интервал (gap), в данном случае используется классическая версия с делением на 2
        for (int gap = n / 2; gap > 0; gap /= 2) {
            // Выполнение сортировки вставками для элементов, отстоящих на интервал gap
            for (int i = gap; i < n; i++) {
                int temp = array[i];
                int j;
                // Сравниваем элементы на расстоянии gap и выполняем вставку
                for (j = i; j >= gap && array[j - gap] > temp; j -= gap) {
                    array[j] = array[j - gap];
                }
                array[j] = temp;
            }
        }
    }

    // Метод для вывода массива на экран
    public static void printArray(int[] array) {
        for (int i : array) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] array = {12, 34, 54, 2, 3, 17, 8, 21, 5};

        System.out.println("Original Array:");
        printArray(array);

        shellSort(array);

        System.out.println("Sorted Array:");
        printArray(array);
    }
}