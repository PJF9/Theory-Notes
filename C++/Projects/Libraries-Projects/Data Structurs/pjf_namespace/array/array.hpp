#ifndef ARRAY
#define ARRAY

#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <typeinfo>

#define ARRAY_GAP 3
#define BAD_ALLOCATION_MESSAGE std::cout << "Error Allocating Memory." << std::endl



// Todo: More remove methods
// Todo: More sorting algorithms



namespace pjf {
    class string;

    template <typename _ArrayType>
    class array {

        private:
            _ArrayType *arr;
            int array_size, extended_size;

            pjf::array<_ArrayType> selection_sort(const bool rev=false);
            pjf::array<_ArrayType> bubble_sort(const bool rev=false);
            pjf::array<_ArrayType> insertion_sort(const bool rev=false);
            pjf::array<_ArrayType> improved_selection_sort(const bool rev=false);

            bool __link_iter_to_vector(std::vector<_ArrayType> &vect, typename std::vector<_ArrayType>::iterator &it) const;
            bool __link_iter_to_vector(const std::vector<_ArrayType> &vect, typename std::vector<_ArrayType>::const_iterator &it) const;
            int __get_random_number(const int min, const int max) const;
            pjf::array<int> __new_indexes() const;

        public:
            class __common_iterator;
            class const_iterator;
            class iterator;

            friend string;

            array();
            array(const std::initializer_list<_ArrayType> &init_list);
            array(const std::vector<_ArrayType> &constructing_vector);
            array(const pjf::array<_ArrayType> &constructing_array);
            array(int total_size, const _ArrayType &value);
            array(const std::string &constructing_string);
            ~array();

            _ArrayType get(int index) const;
            pjf::array<_ArrayType>::iterator get_iter(int index) const;
            pjf::array<_ArrayType>::const_iterator get_citer(int index) const;

            inline int length() const;
            inline int size() const;
            inline _ArrayType *data() const;
            void set_length(int new_size, const _ArrayType &value);
            void set_size(int new_extended_size);
            void shrink();

            pjf::array<_ArrayType> push_back(const _ArrayType &value);
            pjf::array<_ArrayType> push_front(const _ArrayType &value);
            pjf::array<_ArrayType> insert(int index, const _ArrayType &value);
            pjf::array<_ArrayType> insert(pjf::array<_ArrayType>::iterator &position, const _ArrayType &new_value);
            pjf::array<_ArrayType> insert(pjf::array<_ArrayType>::const_iterator &position, const _ArrayType &new_value);
            pjf::array<_ArrayType> extend(const pjf::array<_ArrayType> &aArray);
            pjf::array<_ArrayType> extend(const pjf::array<_ArrayType> &aArray, int start);
            pjf::array<_ArrayType> extend(const std::vector<_ArrayType> &aVector);
            pjf::array<_ArrayType> extend(const std::vector<_ArrayType> &aVector, int start);
            pjf::array<_ArrayType> extend(pjf::array<_ArrayType>::iterator &start, pjf::array<_ArrayType>::iterator &end, const pjf::array<_ArrayType> &iters_object);
            pjf::array<_ArrayType> extend(pjf::array<_ArrayType>::const_iterator &start, pjf::array<_ArrayType>::const_iterator &end, const pjf::array<_ArrayType> &iters_object);
            pjf::array<_ArrayType> extend(typename std::vector<_ArrayType>::iterator &start, typename std::vector<_ArrayType>::iterator &end, std::vector<_ArrayType> &iters_object);
            pjf::array<_ArrayType> extend(typename std::vector<_ArrayType>::const_iterator &start, typename std::vector<_ArrayType>::const_iterator &end, std::vector<_ArrayType> &iters_object);

            pjf::array<_ArrayType> pop_back();
            pjf::array<_ArrayType> pop_front();
            pjf::array<_ArrayType> clear();
            pjf::array<_ArrayType> pop(int index, int total_pos=0); // Go on
            pjf::array<_ArrayType> pop(pjf::array<_ArrayType>::iterator &position);
            pjf::array<_ArrayType> pop(pjf::array<_ArrayType>::const_iterator &position);
            pjf::array<_ArrayType> pop(pjf::array<_ArrayType>::iterator &start, pjf::array<_ArrayType>::iterator &end);
            pjf::array<_ArrayType> pop(pjf::array<_ArrayType>::const_iterator &start, pjf::array<_ArrayType>::const_iterator &end);
            pjf::array<_ArrayType> remove(const _ArrayType &value, bool dupl=false);
            pjf::array<_ArrayType> remove(const pjf::array<_ArrayType> &arr, bool dupl=false);
            pjf::array<_ArrayType> remove(const std::vector<_ArrayType> &vect, bool dupl=false);
            pjf::array<_ArrayType> delete_dupls();
            pjf::array<_ArrayType> set();

            pjf::array<_ArrayType> sort(int sorting_alg=0, bool rev=false);
            pjf::array<_ArrayType> rev_array();
            pjf::array<_ArrayType> rev_array(pjf::array<_ArrayType>::iterator &start, pjf::array<_ArrayType>::iterator &end);
            pjf::array<_ArrayType> rev_array(pjf::array<_ArrayType>::const_iterator &start, pjf::array<_ArrayType>::const_iterator &end);
            pjf::array<_ArrayType> shuffle();
            pjf::array<_ArrayType> copy(const pjf::array<_ArrayType> &ob);
            pjf::array<_ArrayType> copy(const pjf::array<_ArrayType> &ob, int start_i, int end_i);
            pjf::array<_ArrayType> copy(const std::vector<_ArrayType> &ob);
            pjf::array<_ArrayType> copy(const std::vector<_ArrayType> &ob, const int start_i, const int end_i);
            pjf::array<_ArrayType> copy(pjf::array<_ArrayType>::iterator &start, pjf::array<_ArrayType>::iterator &end, const pjf::array<_ArrayType> &iters_object);
            pjf::array<_ArrayType> copy(pjf::array<_ArrayType>::const_iterator &start, pjf::array<_ArrayType>::const_iterator &end, const pjf::array<_ArrayType> &iters_object);
            pjf::array<_ArrayType> copy(typename std::vector<_ArrayType>::iterator &start, typename std::vector<_ArrayType>::iterator &end, std::vector<_ArrayType> &iters_object);
            pjf::array<_ArrayType> copy(typename std::vector<_ArrayType>::const_iterator &start, typename std::vector<_ArrayType>::const_iterator &end, std::vector<_ArrayType> &iters_object);

            std::vector<_ArrayType> to_vector() const;
            const std::vector<_ArrayType> to_cvector() const;
            const pjf::array<_ArrayType> to_carray() const;
            pjf::array<_ArrayType> invoke(_ArrayType (*funct)(_ArrayType));
            pjf::array<_ArrayType> filter(bool (*funct)(_ArrayType));

            int count(const _ArrayType value) const;
            int index(const _ArrayType &value) const;
            int index(const _ArrayType &value, int start, int end, int step=1) const;
            int index(const pjf::array<_ArrayType> &ob) const;
            int index(const std::vector<_ArrayType> &ob) const;
            pjf::array<int> indexes(const _ArrayType &value) const;
            pjf::array<int> indexes(const pjf::array<_ArrayType> &ob) const;
            pjf::array<int> indexes(const std::vector<_ArrayType> &ob) const;
            int last_index(const _ArrayType &value) const;
            int last_index(const pjf::array<_ArrayType> &ob) const;
            int last_index(const std::vector<_ArrayType> &ob) const;
            pjf::array<_ArrayType> swap(int first_index, int second_index);
            pjf::array<_ArrayType> swap(pjf::array<_ArrayType>::iterator &first, pjf::array<_ArrayType>::iterator &second);
            pjf::array<_ArrayType> swap(pjf::array<_ArrayType>::const_iterator &first, pjf::array<_ArrayType>::const_iterator &second);
            pjf::array<_ArrayType> slice(int start, int end, int step=1) const;
            std::string join(const std::string &seperator) const;
            std::string join(char seperator) const;

            iterator begin() const;
            iterator rbegin() const;
            iterator end() const;
            iterator rend() const;
            int at(pjf::array<_ArrayType>::iterator &it) const;
            const const_iterator cbegin() const;
            const const_iterator crbegin() const;
            const const_iterator cend() const;
            const const_iterator crend() const;
            int at(pjf::array<_ArrayType>::const_iterator &it) const;

            inline bool is_equal(const pjf::array<_ArrayType> &right) const;
            inline bool is_equal(const std::vector<_ArrayType> &right) const;
            bool is_symmetric() const;
            inline bool is_empty() const;
            bool is_inside(const _ArrayType &value) const;
            inline bool is_inside(const pjf::array<_ArrayType> &ob) const;
            inline bool is_inside(const std::vector<_ArrayType> &ob) const;

            pjf::array<_ArrayType> &operator=(const pjf::array<_ArrayType> &left);
            pjf::array<_ArrayType> &operator=(const std::vector<_ArrayType> &ob);

            bool operator==(const pjf::array<_ArrayType> &left) const;
            bool operator==(const std::vector<_ArrayType> &left) const;
            inline bool operator!=(const pjf::array<_ArrayType> &left) const;
            inline bool operator!=(const std::vector<_ArrayType> &left) const;
            inline bool operator>(const pjf::array<_ArrayType> &right) const;
            inline bool operator>(const std::vector<_ArrayType> &right) const;
            inline bool operator>=(const pjf::array<_ArrayType> &right) const;
            inline bool operator>=(const std::vector<_ArrayType> &right) const;
            inline bool operator<(const pjf::array<_ArrayType> &right) const;
            inline bool operator<(const std::vector<_ArrayType> &right) const;
            inline bool operator<=(const pjf::array<_ArrayType> &right) const;
            inline bool operator<=(const std::vector<_ArrayType> &right) const;
            
            inline const _ArrayType operator[](const int index) const;
            _ArrayType &operator[](const int index);
            
            pjf::array<_ArrayType> operator+=(int value);
            pjf::array<_ArrayType> operator+=(const pjf::array<_ArrayType> &right);
            pjf::array<_ArrayType> operator+=(const std::vector<_ArrayType> &right);
            pjf::array<_ArrayType> operator-=(int total_indexes);
            pjf::array<_ArrayType> operator-=(const pjf::array<_ArrayType> &right);
            pjf::array<_ArrayType> operator-=(const std::vector<_ArrayType> &right);
            pjf::array<_ArrayType> operator*=(int total_copies);

            pjf::array<_ArrayType> operator+(const _ArrayType value) const;
            pjf::array<_ArrayType> operator+(const pjf::array<_ArrayType> &right) const;
            pjf::array<_ArrayType> operator+(const std::vector<_ArrayType> &right) const;
            pjf::array<_ArrayType> operator-(int value) const;
            pjf::array<_ArrayType> operator-(const pjf::array<_ArrayType> &right) const;
            pjf::array<_ArrayType> operator-(const std::vector<_ArrayType> &right) const;
            pjf::array<_ArrayType> operator*(int value) const;

            pjf::array<_ArrayType> operator++(int);
            pjf::array<_ArrayType> operator++();
            pjf::array<_ArrayType> operator--(int);
            pjf::array<_ArrayType> operator--();

            bool __link_iter_to_arr(typename pjf::array<_ArrayType>::iterator &it);
            bool __link_iter_to_arr(typename pjf::array<_ArrayType>::const_iterator &it);


            class __common_iterator {
                public:
                    _ArrayType *current;

                    bool operator!=(const __common_iterator &element) const;
                    bool operator==(const __common_iterator &element) const;
                    bool operator==(const typename std::vector<_ArrayType>::iterator &element) const;
                    bool operator>(const __common_iterator &_it) const;
                    bool operator>=(const __common_iterator &_it) const;
                    bool operator<(const __common_iterator &_it) const;
                    bool operator<=(const __common_iterator &_it) const;
                    __common_iterator &operator++();
                    __common_iterator &operator--();
                    __common_iterator &operator++(int);
                    __common_iterator &operator--(int);
            };

            class const_iterator: public __common_iterator {
                public:
                    const_iterator();
                    const_iterator(_ArrayType *elem);
                    const _ArrayType &operator*() const;
                    const const_iterator operator+(int value) const;
                    const const_iterator operator-(int value) const;
            };

            class iterator: public __common_iterator {
                public:
                    iterator();
                    iterator(_ArrayType *elem);
                    _ArrayType& operator*();
                    iterator& operator+=(int value);
                    iterator& operator-=(int value);
                    iterator operator+(int value);
                    iterator operator-(int value);
            };

            template <typename _Type> friend std::ostream &operator<<(std::ostream &left, const pjf::array<_Type> &ob);
            template <typename _Type> friend std::istream &operator>>(std::istream &left, const pjf::array<_Type> &ob);
    };
}

#include "array_in.inl"
#include "array_code.cpp"
#endif
