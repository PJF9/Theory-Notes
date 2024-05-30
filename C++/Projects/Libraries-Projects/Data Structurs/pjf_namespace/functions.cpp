#include "array/array.hpp"


namespace pjf {
    template <typename _ArrayType> bool iter_link_to_array(const pjf::array<_ArrayType> &arr, typename pjf::array<_ArrayType>::iterator &it);
    template <typename _ArrayType> bool iter_link_to_array(const pjf::array<_ArrayType> &arr, typename pjf::array<_ArrayType>::const_iterator &it);
    template <typename _ArrayType> bool iter_link_to_array(const std::vector<_ArrayType> &vect, typename std::vector<_ArrayType>::iterator &it);
    template <typename _ArrayType> bool iter_link_to_array(const std::vector<_ArrayType> &vect, typename std::vector<_ArrayType>::const_iterator &it);

    template <typename _ArrayType> pjf::array<_ArrayType> to_array(const std::vector<_ArrayType> &vect);
    template <typename _ArrayType> pjf::array<_ArrayType> to_array(const _ArrayType arr[], const int size);
    template <typename _ArrayType> std::vector<_ArrayType> to_vector(const pjf::array<_ArrayType> &arr);
    template <typename _ArrayType> std::vector<_ArrayType> to_vector(const _ArrayType arr[], const int size);

    template <typename _CheckType, typename _ObjectType> inline bool isinstance(const _ObjectType &obj); // usage: pjf::isinstance <check_type> (object)

    template <typename _ArrayType> int sum(const pjf::array<_ArrayType> &arr);
    template <typename _ArrayType> int sum(const std::vector<_ArrayType> &vect);
    template <typename _ArrayType> int max(const pjf::array<_ArrayType> &arr);
    template <typename _ArrayType> int max(const std::vector<_ArrayType> &vect);
    template <typename _ArrayType> int min(const pjf::array<_ArrayType> &arr);
    template <typename _ArrayType> int min(const std::vector<_ArrayType> &vect);

    template <typename _ArrayType> pjf::array<_ArrayType> invoke(pjf::array<_ArrayType> &arr, _ArrayType (*funct)(_ArrayType));
    template <typename _ArrayType> std::vector<_ArrayType> invoke(std::vector<_ArrayType> &vect, _ArrayType (*funct)(_ArrayType));
    template <typename _ArrayType> pjf::array<_ArrayType> filter(pjf::array<_ArrayType> &arr, bool (*funct)(_ArrayType));
    template <typename _ArrayType> std::vector<_ArrayType> filter(std::vector<_ArrayType> &vect, bool (*funct)(_ArrayType));

    int get_cstring_size(const char* string);
}










template <typename _ArrayType>
bool pjf::iter_link_to_array(const pjf::array<_ArrayType> &arr, typename pjf::array<_ArrayType>::iterator &it) {
    for (typename pjf::array<_ArrayType>::iterator arr_it=arr.begin(); arr_it!=arr.end(); arr_it++) {
        if (arr_it == it) {
            return true;
        }
    }
    return false;
}





template <typename _ArrayType>
bool pjf::iter_link_to_array(const pjf::array<_ArrayType> &arr, typename pjf::array<_ArrayType>::const_iterator &it) {
    for (typename pjf::array<_ArrayType>::const_iterator arr_it=arr.cbegin(); arr_it!=arr.cend(); arr_it++) {
        if (arr_it == it) {
            return true;
        }
    }
    return false;
}





template <typename _ArrayType>
bool pjf::iter_link_to_array(const std::vector<_ArrayType> &vect, typename std::vector<_ArrayType>::iterator &it) {
    for (typename std::vector<_ArrayType>::const_iterator vect_it=vect.begin(); vect_it!=vect.end(); vect_it++) {
        if (vect_it == it) {
            return true;
        }
    }
    return false;
}





template <typename _ArrayType>
bool pjf::iter_link_to_array(const std::vector<_ArrayType> &vect, typename std::vector<_ArrayType>::const_iterator &it) {
    for (typename std::vector<_ArrayType>::const_iterator vect_it=vect.cbegin(); vect_it!=vect.cend(); vect_it++) {
        if (vect_it == it) {
            return true;
        }
    }
    return false;
}





template <typename _ArrayType>
std::vector<_ArrayType> pjf::to_vector(const pjf::array<_ArrayType> &arr) {
    std::vector<_ArrayType> temp;
    for (int i=0; i<arr.length(); i++) {
        temp.push_back(arr[i]);
    }

    return temp;
}





template <typename _ArrayType>
pjf::array<_ArrayType> pjf::to_array(const std::vector<_ArrayType> &vect) {
    return pjf::array<_ArrayType> (vect);
}





template <typename _ArrayType>
pjf::array<_ArrayType> pjf::to_array(const _ArrayType arr[], const int size) {
    pjf::array<_ArrayType> temp;
    for (int i=0; i<size; i++) {
        temp.push_back(arr[i]);
    }

    return temp;
}





template <typename _ArrayType>
std::vector<_ArrayType> pjf::to_vector(const _ArrayType arr[], const int size) {
    std::vector<_ArrayType> temp;
    for (int i=0; i<size; i++) {
        temp.push_back(arr[i]);
    }

    return temp;
}





template <typename _CheckType, typename _ObjectType> 
bool pjf::isinstance(const _ObjectType &obj) {
    return (*typeid(_CheckType).name() == *typeid(_ObjectType).name()) ? true : false;
}





template <typename _ArrayType>
int pjf::sum(const pjf::array<_ArrayType> &arr) {
    if (arr.is_empty()) {
        std::cout << "Array is empty." << std::endl;
        return -1;
    }

    if (*typeid(_ArrayType).name() == *typeid(int).name()) {
        int x = 0;
        for (int elem: arr) {
            x += elem;
        }
        return x;
    }

    std::cout << "Only 'int' type arrays are quilified for 'sum' function." << std::endl;
    return -1;
}





template <typename _ArrayType>
int pjf::sum(const std::vector<_ArrayType> &vect) {
    if (vect.size() == 0) {
        std::cout << "Vector is empty." << std::endl;
        return -1;
    }

    if (*typeid(_ArrayType).name() == *typeid(int).name()) {
        int x = 0;
        for (int elem: vect) {
            x += elem;
        }
        return x;
    }

    std::cout << "Only 'int' type arrays are quilified for 'sum' function." << std::endl;
    return -1;
}





template <typename _ArrayType>
int pjf::max(const pjf::array<_ArrayType> &arr) {
    if (arr.is_empty()) {
        std::cout << "Array is empty." << std::endl;
        return -1;
    }

    if (*typeid(_ArrayType).name() == *typeid(int).name()) {
        int max = arr[0];
        for (int elem: arr) {
            if (elem > max) {
                max = elem;
            }
        }
        return max;
    }

    std::cout << "Only 'int' type arrays are quilified for 'max' function." << std::endl;
    return -1;
}





template <typename _ArrayType>
int pjf::max(const std::vector<_ArrayType> &vect) {
    if (vect.size() == 0) {
        std::cout << "vector is empty." << std::endl;
        return -1;
    }

    if (*typeid(_ArrayType).name() == *typeid(int).name()) {
        int max = vect[0];
        for (int elem: vect) {
            if (elem > max) {
                max = elem;
            }
        }
        return max;
    }

    std::cout << "Only 'int' type arrays are quilified for 'max' function." << std::endl;
    return -1;
}





template <typename _ArrayType>
int pjf::min(const pjf::array<_ArrayType> &arr) {
    if (arr.is_empty()) {
        std::cout << "Array is empty." << std::endl;
        return -1;
    }

    if (*typeid(_ArrayType).name() == *typeid(int).name()) {
        int min = arr[0];
        for (size_t elem: arr) {
            if (elem < min) {
                min = elem;
            }
        }
        return min;
    }

    std::cout << "Only 'int' type arrays are quilified for 'min' function." << std::endl;
    return -1;
}





template <typename _ArrayType>
int pjf::min(const std::vector<_ArrayType> &vect) {
    if (vect.size() == 0) {
        std::cout << "Vector is empty." << std::endl;
        return -1;
    }

    if (*typeid(_ArrayType).name() == *typeid(int).name()) {
        int min = vect[0];
        for (size_t elem: vect) {
            if (elem < min) {
                min = elem;
            }
        }
        return min;
    }

    std::cout << "Only 'int' type arrays are quilified for 'min' function." << std::endl;
    return -1;   
}





template <typename _ArrayType>
pjf::array<_ArrayType> pjf::invoke(pjf::array<_ArrayType> &arr, _ArrayType (*funct)(_ArrayType)) {
    for (int i=0; i<arr.length(); i++) {
        arr[i] = funct(arr[i]);
    }

    return arr;
}





template <typename _ArrayType>
std::vector<_ArrayType> pjf::invoke(std::vector<_ArrayType> &vect, _ArrayType (*funct)(_ArrayType)) {
    for (int i=0; i<vect.size(); i++) {
        vect[i] = funct(vect[i]);
    }

    return vect;
}





template <typename _ArrayType>
pjf::array<_ArrayType> pjf::filter(pjf::array<_ArrayType> &arr, bool (*funct)(_ArrayType)) {
    _ArrayType *temp = new(std::nothrow) _ArrayType[arr.length()];
    if (!temp) {std::cout << "Error Allocating Memory." << std::endl; exit(0);}

    int j = 0;
    for (int i=0; i<arr.length(); i++) {
        if (funct(arr[i])) {
            temp[j] = arr[i];
            j++;
        }
    }

    arr.clear();

    for (int i=0; i<j; i++) {
        arr.push_back(temp[i]);
    }

    delete[] temp;

    return arr;
}





template <typename _ArrayType>
std::vector<_ArrayType> pjf::filter(std::vector<_ArrayType> &vect, bool (*funct)(_ArrayType)) {
    _ArrayType *temp = new(std::nothrow) _ArrayType[vect.size()];
    if (!temp) {std::cout << "Error Allocating Memory." << std::endl; exit(0);}

    int j = 0;
    for (int i=0; i<vect.size(); i++) {
        if (funct(vect[i])) {
            temp[j] = vect[i];
            j++;
        }
    }

    vect.clear();

    for (int i=0; i<j; i++) {
        vect.push_back(temp[i]);
    }

    delete[] temp;

    return vect;
}





int pjf::get_cstring_size(const char* string) {
    int index = 0;
    while (string[index] != '\0') {
        index ++;
    }

    return index;
}
