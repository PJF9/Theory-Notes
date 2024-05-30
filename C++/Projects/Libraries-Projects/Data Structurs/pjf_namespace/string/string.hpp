#ifndef STRING
#define STRING

#include "../array/array.hpp"


namespace pjf {

    class string {
        private:
            pjf::array<char> s;

            int __char_to_int(const char &letter) const;
            int __get_cstring_size(const char *cstring) const;
            int __get_iter_index(std::string &str, typename std::string::iterator &it) const;
            int __get_iter_index(const std::string &str, typename std::string::const_iterator &it) const;

        public:
            class __common_iterator;
            class iterator;
            class const_iterator;

            string();
            string(const char &letter);
            string(const char *cstring);
            string(const pjf::string &str);
            string(const std::string &str);
            string(const pjf::array<int> &ascii_arr);
            ~string();

            char get(int index) const;
            inline int iget(int index) const;
            pjf::string::iterator get_iter(int index) const;
            pjf::string::const_iterator get_citer(int index) const;

            inline int length() const;
            inline int size() const;
            inline char *data() const;
            void set_length(int new_size, const char &letter);
            void set_size(int new_size);
            void change_capacity(int new_extended_size);
            inline void shrink();

            pjf::string push_back(const char &letter);
            pjf::string push_front(const char &letter);
            pjf::string insert(int index, const char &letter);
            pjf::string insert(pjf::string::iterator &position, const char &new_letter);
            pjf::string insert(pjf::string::const_iterator &position, const char &new_letter);
            pjf::string extend(const char *cstring);
            pjf::string extend(const std::string &str);
            pjf::string extend(const pjf::string &str);
            pjf::string extend(const char *cstring, int index);
            pjf::string extend(const std::string &str, int index);
            pjf::string extend(const pjf::string &str, int index);
            pjf::string extend(pjf::string::iterator &start, pjf::string::iterator &end, pjf::string &iters_object);
            pjf::string extend(pjf::string::const_iterator &start, pjf::string::const_iterator &end, pjf::string &iters_object);
            pjf::string extend(std::string::iterator &start, std::string::iterator &end, std::string &iters_object);
            pjf::string extend(std::string::const_iterator &start, std::string::const_iterator &end, std::string &iters_object);

            pjf::string replace(int index, const char &letter);
            pjf::string replace(int index, const char *cstring);
            pjf::string replace(int index, const std::string &str);
            pjf::string replace(int index, const pjf::string &str);
            pjf::string replace(int index, int total_pos, const char &letter);
            pjf::string replace(const char &letter1, const char &letter2);
            pjf::string replace(typename pjf::string::iterator &it, const char &new_letter);
            pjf::string replace(typename pjf::string::iterator &it, const char *cstring);
            pjf::string replace(typename pjf::string::iterator &it, const std::string &str);
            pjf::string replace(typename pjf::string::iterator &it, const pjf::string &str);
            pjf::string replace(typename pjf::string::const_iterator &it, const char &new_letter);
            pjf::string replace(typename pjf::string::const_iterator &it, const char *cstring);
            pjf::string replace(typename pjf::string::const_iterator &it, const std::string &str);
            pjf::string replace(typename pjf::string::const_iterator &it, const pjf::string &str);
            pjf::string replace(typename pjf::string::iterator &it, int total_pos, const char &letter);
            pjf::string replace(typename pjf::string::const_iterator &it, int total_pos, const char &letter);

            pjf::string pop_back();
            pjf::string pop_front();
            pjf::string clear();
            pjf::string pop(int index, int total_pos=0);
            pjf::string pop(typename pjf::string::iterator &it);
            pjf::string pop(typename pjf::string::const_iterator &it);
            pjf::string pop(typename pjf::string::iterator &start, typename pjf::string::iterator &end);
            pjf::string pop(typename pjf::string::const_iterator &start, typename pjf::string::const_iterator &end);
            pjf::string remove(const char &letter, bool dupl=false);
            pjf::string remove(const char *cstring, bool dupl=false);
            pjf::string remove(const std::string &str, bool dupl=false);
            pjf::string remove(const pjf::string &str, bool dupl=false);
            pjf::string delete_dupls();

            pjf::string rev_string();
            pjf::string rev_string(typename pjf::string::iterator &start, typename pjf::string::iterator &end);
            pjf::string rev_string(typename pjf::string::const_iterator &start, typename pjf::string::const_iterator &end);
            pjf::string shuffle();
            pjf::string adjust_left(int new_length, const char &filler='_');
            pjf::string adjust_right(int new_length, const char &filler='_');
            template <typename _Type> pjf::string format(const std::initializer_list<_Type> &il);
            pjf::string copy(const char &letter);
            pjf::string copy(const char *cstring);
            pjf::string copy(const char *cstring, int start_i, int end_i);
            pjf::string copy(const std::string &str);
            pjf::string copy(const std::string &str, int start_i, int end_i);
            pjf::string copy(const pjf::string &str);
            pjf::string copy(const pjf::string &str, int start_i, int end_i);
            pjf::string copy(typename pjf::string::iterator &start, typename pjf::string::iterator &end, pjf::string &iters_object);
            pjf::string copy(typename pjf::string::const_iterator &start, typename pjf::string::const_iterator &end, pjf::string &iters_object);
            pjf::string copy(typename std::string::iterator &start, typename std::string::iterator &end, std::string &iters_object);
            pjf::string copy(typename std::string::const_iterator &start, typename std::string::const_iterator &end, const std::string &iters_object);

            std::string to_std_string() const;
            const char* to_cstring() const;
            pjf::array<char> to_array() const;
            pjf::array<int> give_ascii() const;
            pjf::string to_upper();
            pjf::string to_upper(int start_i, int end_i);
            pjf::string to_lower();
            pjf::string to_lower(int start_i, int end_i);
            pjf::string swap_case();
            pjf::string swap_case(int start_i, int end_i);
            int to_int() const;
            pjf::string capitalize();
            pjf::string title();

            pjf::string swap(int first_i, int second_i);
            pjf::string swap(pjf::string &str);
            pjf::string swap(std::string &str);
            pjf::string slice(int start, int end, int step=1) const;
            pjf::string center(int new_length, const char &filler=' ');
            pjf::string ltrim();
            pjf::string rtrim();
            pjf::string trim();

            int count(const char &letter) const;
            int index(const char &letter) const;
            int index(const char *cstring) const;
            int index(const std::string &str) const;
            int index(const pjf::string &str) const;
            pjf::array<int> indexes(const char &letter) const;
            pjf::array<int> indexes(const char *cstring) const;
            pjf::array<int> indexes(const std::string &str) const;
            pjf::array<int> indexes(const pjf::string &str) const;
            int last_index(const char &letter) const;
            int last_index(const char *cstring) const;
            int last_index(const std::string &str) const;
            int last_index(const pjf::string &str) const;

            pjf::array<char> split() const;
            pjf::array<pjf::string> split(const char &letter) const;
            pjf::array<pjf::string> split(const char *cstring) const;
            pjf::array<pjf::string> split(const std::string &str) const;
            pjf::array<pjf::string> split(const pjf::string &str) const;
            pjf::array<pjf::string> partion(const char &letter) const;
            pjf::array<pjf::string> partion(const char *cstring) const;
            pjf::array<pjf::string> partion(const std::string &str) const;
            pjf::array<pjf::string> partion(const pjf::string &str) const;

            inline char first() const;
            inline char last() const;

            inline iterator begin() const;
            inline iterator end() const;
            inline iterator rbegin() const;
            inline iterator rend() const;
            int at(pjf::string::iterator &it) const;
            inline const const_iterator cbegin() const;
            inline const const_iterator cend() const;
            inline const const_iterator crbegin() const;
            inline const const_iterator crend() const;
            int at(pjf::string::const_iterator &it) const;

            inline bool is_inside(const char &letter) const;
            inline bool is_inside(const char *cstring) const;
            inline bool is_inside(const std::string &str) const;
            inline bool is_inside(const pjf::string &str) const;
            inline bool is_empty() const;
            bool startswith(const char &letter) const;
            bool startswith(const char *cstring) const;
            bool startswith(const std::string &str) const;
            bool startswith(const pjf::string &str) const;
            bool endswith(const char &letter) const;
            bool endswith(const char *cstring) const;
            bool endswith(const std::string &str) const;
            bool endswith(const pjf::string &str) const;
            bool is_digit() const;
            bool is_num() const;
            bool is_special() const;
            bool is_alpharithmetic() const;
            bool is_space() const;
            bool is_upper() const;
            bool is_lower() const;
            bool is_capitalize() const;
            bool is_title() const;
            inline bool is_palindrome() const;

            bool non_case_comparison(const char *symbol, const char &letter) const;
            bool non_case_comparison(const char *symbol, const char *cstring) const;
            bool non_case_comparison(const char *symbol, const std::string &str) const;
            bool non_case_comparison(const char *symbol, const pjf::string &str) const;

            inline bool is_longer(const char &letter) const;
            inline bool is_longer(const char *cstring) const;
            inline bool is_longer(const std::string &str) const;
            inline bool is_longer(const pjf::string &str) const;
            inline bool is_longer_or_equal(const char &letter) const;
            inline bool is_longer_or_equal(const char *cstring) const;
            inline bool is_longer_or_equal(const std::string &str) const;
            inline bool is_longer_or_equal(const pjf::string &str) const;
            inline bool is_shorter(const char &letter) const;
            inline bool is_shorter(const char *cstring) const;
            inline bool is_shorter(const std::string &str) const;
            inline bool is_shorter(const pjf::string &str) const;
            inline bool is_shorter_or_equal(const char &letter) const;
            inline bool is_shorter_or_equal(const char *cstring) const;
            inline bool is_shorter_or_equal(const std::string &str) const;
            inline bool is_shorter_or_equal(const pjf::string &str) const;
            inline bool same_length(const char &letter) const;
            inline bool same_length(const char *cstring) const;
            inline bool same_length(const std::string &str) const;
            inline bool same_length(const pjf::string &str) const;

            char &operator[](int index);
            inline char operator[](int index) const;

            pjf::string &operator=(const char &letter);
            pjf::string &operator=(const char *cstring);
            pjf::string &operator=(const std::string &str);
            pjf::string &operator=(const pjf::string &str);

            bool operator==(const char &letter) const;
            bool operator==(const char *cstring) const;
            bool operator==(const std::string &str) const;
            bool operator==(const pjf::string &str) const;
            inline bool operator!=(const char &letter) const;
            inline bool operator!=(const char *cstring) const;
            inline bool operator!=(const std::string &str) const;
            inline bool operator!=(const pjf::string &str) const;
            bool operator>(const char &letter) const;
            bool operator>(const char *cstring) const;
            bool operator>(const std::string &str) const;
            bool operator>(const pjf::string &str) const;
            bool operator>=(const char &letter) const;
            bool operator>=(const char *cstring) const;
            bool operator>=(const std::string &str) const;
            bool operator>=(const pjf::string &str) const;
            bool operator<(const char &letter) const;
            bool operator<(const char *cstring) const;
            bool operator<(const std::string &str) const;
            bool operator<(const pjf::string &str) const;
            bool operator<=(const char &letter) const;
            bool operator<=(const char *cstring) const;
            bool operator<=(const std::string &str) const;
            bool operator<=(const pjf::string &str) const;

            pjf::string operator+=(int positions);
            pjf::string operator+=(const char &letter);
            pjf::string operator+=(const char *cstring);
            pjf::string operator+=(const std::string &str);
            pjf::string operator+=(const pjf::string &str);
            pjf::string operator-=(int positions);
            pjf::string operator-=(const char &letter);
            pjf::string operator-=(const char *cstring);
            pjf::string operator-=(const std::string &str);
            pjf::string operator-=(const pjf::string &str);
            pjf::string operator*=(int total_times);

            pjf::string operator+(int positions) const;
            pjf::string operator+(const char &letter) const;
            pjf::string operator+(const char *cstring) const;
            pjf::string operator+(const std::string &str) const;
            pjf::string operator+(const pjf::string &str) const;
            pjf::string operator-(int positions) const;
            pjf::string operator-(const char &letter) const;
            pjf::string operator-(const char *cstring) const;
            pjf::string operator-(const std::string &str) const;
            pjf::string operator-(const pjf::string &str) const;
            pjf::string operator*(int total_times) const;

            pjf::string operator++(int);
            pjf::string operator++();
            pjf::string operator--(int);
            pjf::string operator--();

            int __get_iter_index(string &str, typename string::iterator &it) const;
            int __get_iter_index(const string &str, typename string::const_iterator &it) const;
            bool __iter_link_to_string(string &str, string::iterator &it) const;
            bool __iter_link_to_string(const string &str, string::const_iterator &it) const;


            class __common_iterator {
                public:
                    char *current;

                    inline bool operator==(const __common_iterator &_it) const;
                    inline bool operator!=(const __common_iterator &_it) const;
                    inline bool operator>(const __common_iterator &_it) const;
                    inline bool operator>=(const __common_iterator &_it) const;
                    inline bool operator<(const __common_iterator &_it) const;
                    inline bool operator<=(const __common_iterator &_it) const;
                    __common_iterator &operator++();
                    __common_iterator &operator++(int);
                    __common_iterator &operator--();
                    __common_iterator &operator--(int);
            };

            class const_iterator: public pjf::string::__common_iterator {
                public:
                    const_iterator();
                    const_iterator(char *elem);
                    inline const char &operator*() const;
                    const const_iterator operator+(const int value) const;
                    const const_iterator operator-(const int value) const;
            };

            class iterator: public pjf::string::__common_iterator {
                public:
                    iterator();
                    iterator(char *elem);
                    inline char &operator*() const;
                    iterator &operator+=(const int value);
                    iterator &operator-=(const int value);
                    iterator operator+(const int value) const;
                    iterator operator-(const int value) const;
            };


            friend std::ostream &operator<<(std::ostream &left, const pjf::string &str) {
                if (str.length() <= 1) {
                    left << "\'";
                    for (int i=0; i<str.length(); i++) {
                        left << str.get(i);
                    }
                    left << "\'";
                }
                else {
                    left << "\"";
                    for (int i=0; i<str.length(); i++) {
                        left << str.get(i);
                    }
                    left << "\"";
                }

                return left;
            }
    
            friend std::istream &operator>>(std::istream &left, pjf::string &str) {
                std::string user_input;
                getline(left, user_input);

                str += user_input;

                return left;
            }
    };
}


#include "string_in.inl"
#include "string_code.cpp"
#endif
