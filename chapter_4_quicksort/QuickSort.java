import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class QuickSort {

    private List<Integer> quickSort(List<Integer> numbers) {
        if (numbers.size() < 2) {
            return numbers;
        }

        int pivot = numbers.get(0);

        List<Integer> less = numbers.subList(1, numbers.size())
                .stream()
                .filter(n -> n <= pivot)
                .collect(Collectors.toList());

        List<Integer> greater = numbers.subList(1, numbers.size())
                .stream()
                .filter(n -> n > pivot)
                .collect(Collectors.toList());

        quickSort(less).add(pivot);
        less.addAll(quickSort(greater));

        return less;
    }

    private void quickSort2(int[] arr, int begin, int end) {
        if (begin < end) {
            int partitionIndex = partition(arr, begin, end);
            quickSort2(arr, begin, partitionIndex-1);
            quickSort2(arr, partitionIndex+1, end);
        }
    }

    private int partition(int[] arr, int begin, int end) {
        int pivot = arr[end];
        int i = begin - 1;

        for (int j = begin; j < end; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        i++;
        int temp = arr[i];
        arr[i] = arr[end];
        arr[end] = temp;

        return i;
    }

    private void printArray(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<Integer>(Arrays.asList(5, 10, -12, 300, 4, 8));

        QuickSort app = new QuickSort();

        System.out.println(app.quickSort(numbers));

        int arr[] = {5, 10, -12, 300, 4, 8};
        app.quickSort2(arr, 0, arr.length-1);
        app.printArray(arr);
    }

}
