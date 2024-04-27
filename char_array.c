{{{}}}
//standard libraries
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>
//Windows
#include <windows.h>

// #include "string_defines.h"
/**
 * @file char_array.c
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2024-04-24
 * 
 * @copyright Copyright (c) 2024
 * 
 * multi-line comment
 * 
 */
#include "Libraries/string/src/string_defines.h"


typedef struct string_data_type_char{
    int memory_size;
    int string_size;
    char* string;
} string_data_type_char;
typedef struct string_data_type_unsigned_char{
    int memory_size;
    int string_size;
    unsigned char* string;
} string_data_type_unsigned_char;

void string_print(char* string1){

    printf("%s\n", string1);

}
void string_print_char(char* string1){

    string_print(string1);

}
void string_print_const_char(const char* string1){

    printf("%s\n", string1);

}
void string_print_message_before_char(char* string1, const char* messageBeforeOutput){

    printf("%s%s\n", messageBeforeOutput, string1);

}
void string_print_message_before_const_char(const char* string1, const char* messageBeforeOutput){

    printf("%s%s\n", messageBeforeOutput, string1);

}

void string_set_null(char* string){
    string[0] = '\0';
}
char* string_create(int size){

    char* string = (char*)malloc(size*sizeof(char) + 1);
    string_set_null(string);
    return string;

}
void string_delete(char* string){

    free(string);

}

bool string_compare_my_realisation_char_char(char* string1, char* string2){
    bool temp = true;
    bool compare_result = false;
    for(int i = 0; temp == true; i++){
        if(string1[i] == '\0' || string2[i] == '\0'){
            temp = false;
        }
        if(string1[i] == string2[i]){
            compare_result = true;
        } 
        else{
            compare_result = false;
            temp = false;
        }
    }
    return compare_result;
}
bool string_compare_my_realisation_const_char_char(const char* string1, char* string2){
    bool temp = true;
    bool compare_result = false;
    for(int i = 0; temp == true; i++){
        if(string1[i] == '\0' || string2[i] == '\0'){
            temp = false;
        }
        if(string1[i] == string2[i]){
            compare_result = true;
        } 
        else{
            compare_result = false;
            temp = false;
        }
    }
    return compare_result;
}
bool string_compare_my_realisation_char_const_char(char* string1, const char* string2){
    bool temp = true;
    bool compare_result = false;
    for(int i = 0; temp == true; i++){
        if(string1[i] == '\0' || string2[i] == '\0'){
            temp = false;
        }
        if(string1[i] == string2[i]){
            compare_result = true;
        } 
        else{
            compare_result = false;
            temp = false;
        }
    }
    return compare_result;
}
bool string_compare_my_realisation_const_char_const_char(const char* string1, const char* string2){
    bool temp = true;
    bool compare_result = false;
    for(int i = 0; temp == true; i++){
        if(string1[i] == '\0' || string2[i] == '\0'){
            temp = false;
        }
        if(string1[i] == string2[i]){
            compare_result = true;
        } 
        else{
            compare_result = false;
            temp = false;
        }
    }
    return compare_result;
}
bool string_compare(char* string1, char* string2){

    bool result = false;
    if(strcmp(string1, string2) == 0){
        result = true;
    }
    else{
        result = false;
    }
    return result;

}
bool string_compare_char(char* string1, char* string2){

    bool result = false;
    if(strcmp(string1, string2) == 0){
        result = true;
    }
    else{
        result = false;
    }
    return result;

}
bool string_compare_const_char(char* string1, const char* string2){

    bool result = false;
    if(strcmp(string1, string2) == 0){
        result = true;
    }
    else{
        result = false;
    }
    return result;

}
bool string_compare_char_char(char* string1, const char* string2){

    bool result = false;
    if(strcmp(string1, string2) == 0){
        result = true;
    }
    else{
        result = false;
    }
    return result;

}
bool string_compare_const_char_char(const char* string1, char* string2){

    bool result = false;
    if(strcmp(string1, string2) == 0){
        result = true;
    }
    else{
        result = false;
    }
    return result;

}
bool string_compare_char_const_char(char* string1, const char* string2){

    bool result = false;
    if(strcmp(string1, string2) == 0){
        result = true;
    }
    else{
        result = false;
    }
    return result;

}
bool string_compare_const_char_const_char(const char* string1, const char* string2){

    bool result = false;
    if(strcmp(string1, string2) == 0){
        result = true;
    }
    else{
        result = false;
    }
    return result;

}
bool string_compare_char_char2(char* string1, char* string2){

    return string_compare_my_realisation_char_char(string1, string2);

}
bool string_compare_const_char_char2(const char* string1, char* string2){

    return string_compare_my_realisation_const_char_char(string1, string2);

}
bool string_compare_char_const_char2(char* string1, const char* string2){

    return string_compare_my_realisation_char_const_char(string1, string2);

}
bool string_compare_const_const_char_const_char2(const char* string1, const char* string2){

    return string_compare_my_realisation_const_char_const_char(string1, string2);

}

int string_get_size(char* string){

    bool condition = true;
    int string_size = 0;
    for(int i = 0; condition == true; i++){
        if(string[i] == '\0'){
            condition = false;
        }
        else{
            string_size++;
        }
    }
    return string_size;

}
int string_get_size_char(char* string){

    return string_get_size(string);

}
int string_get_size_const_char(const char* string){

    bool cond = true;
    int string_size = 0;
    for(int i = 0; cond == true; i++){
        if(string[i] == '\0'){
            cond = false;
        }
        else{
            string_size++;
        }
    }
    return string_size;

}

void string_add(char* string, char symbol){

    int string_size = string_get_size(string);
    string[string_size] = symbol;
    string[string_size+1] = '\0';

}
void string_append(char* string, char symbol){

    string_add(string, symbol);

}

char* string_shift(char* string, int start, int counts, int end, char* string_to_write, int action){

    if(action == shift_left || action == shift_left_fill){

        for(int i = start; i<=end; i++){
            if(i - counts >= 0){
                string[i - counts] = string[i];
            }
        }

        if(end - counts < 0 && action == shift_left_fill){
            for(int i = 0; i<=end; i++){
                string[i] = '_';
            }
        }
        else if(end - counts >= 0 && action == shift_left_fill){
            for(int i = end - counts + 1; i<=end; i++){
                string[i] = '_';
            }
        }

    }
    else if(action == shift_right || action == shift_right_fill){

        for(int i = end; i>=start; i--){
            string[i + counts] = string[i];
        }
        string[end + counts + 1] = '\0';

        if(action == shift_right_fill){
            for(int i = start; i<start+counts; i++){
                string[i] = '_';
            }
        }

    }
    else if(action == read){

        char* temp = string_create(end-start+1);
        for(int i = start; i<=end; i++){
            temp[i - start] = string[i];
        }
        // temp[end] = '\0';
        // temp[end-1] = '\0';
        // temp[end+1] = '\0';
        temp[end-start+1] = '\0';

        return temp;

    }
    else if(action == write){

        for(int i = start; i<=end; i++){
            string[i] = string_to_write[i - start];
        }

    }
    else if(action == none){

        //doing nothing

    }

    return string;

}
char* string_shift_const_char(char* string, int start, int counts, int end, const char* string_to_write, int action){

    if(action == shift_left || action == shift_left_fill){

        for(int i = start; i<=end; i++){
            if(i - counts >= 0){
                string[i - counts] = string[i];
            }
        }

        if(end - counts < 0 && action == shift_left_fill){
            for(int i = 0; i<=end; i++){
                string[i] = '_';
            }
        }
        else if(end - counts >= 0 && action == shift_left_fill){
            for(int i = end - counts + 1; i<=end; i++){
                string[i] = '_';
            }
        }

    }
    else if(action == shift_right || action == shift_right_fill){

        for(int i = end; i>=start; i--){
            string[i + counts] = string[i];
        }
        string[end + counts + 1] = '\0';

        if(action == shift_right_fill){
            for(int i = start; i<start+counts; i++){
                string[i] = '_';
            }
        }

    }
    else if(action == read){

        char* temp = string_create(end-start+1);
        for(int i = start; i<=end; i++){
            temp[i - start] = string[i];
        }
        // temp[end] = '\0';
        // temp[end-1] = '\0';
        // temp[end+1] = '\0';
        temp[end-start+1] = '\0';

        return temp;

    }
    else if(action == write){

        for(int i = start; i<=end; i++){
            string[i] = string_to_write[i - start];
        }

    }
    else if(action == none){

        //doing nothing

    }

    return string;

}
bool string_shift_left(char* string, int start, int count){
    int start2 = start;
    int length2 = string_get_size(string) - start;
    int shift_way2 = count;
    int end2 = length2 + start2 - 1;
    char* empty_string = NULL;
    string_shift(string, start2, shift_way2, end2, empty_string, shift_left);
    return true;
}
bool string_shift_left_fill(char* string, int start, int count){
    int start2 = start;
    int length2 = string_get_size(string) - start;
    int shift_way2 = count;
    int end2 = length2 + start2 - 1;
    char* empty_string = NULL;
    string_shift(string, start2, shift_way2, end2, empty_string, shift_left_fill);
    return false;
}
bool string_shift_right(char* string, int start, int count){
    int start2 = start;
    int length2 = string_get_size(string) - start;
    int shift_way2 = count;
    int end2 = length2 + start2 - 1;
    char* empty_string = NULL;
    string_shift(string, start2, shift_way2, end2, empty_string, shift_right);
    return false;
}
bool string_shift_right_fill(char* string, int start, int count){
    int start2 = start;
    int length2 = string_get_size(string) - start;
    int shift_way2 = count;
    int end2 = length2 + start2 - 1;
    char* empty_string = NULL;
    string_shift(string, start2, shift_way2, end2, empty_string, shift_right_fill);
    return false;
}
bool string_shift_write(char* string, int start, int length, char* string_for_write){
    int start2 = start;
    int length2 = length;
    int shift_way2 = 1;
    int end2 = length2 + start2 - 1;
    string_shift(string, start2, shift_way2, end2, string_for_write, write);
    return false;
}
bool string_shift_write_const_char(char* string, int start, int length, const char* string_for_write){
    int start2 = start;
    int length2 = length;
    int shift_way2 = 1;
    int end2 = length2 + start2 - 1;
    string_shift_const_char(string, start2, shift_way2, end2, string_for_write, write);
    return false;
}
char* string_shift_read(char* string, int start, int length){
    int start2 = start;
    int length2 = length;
    int shift_way2 = string_get_size(string) - start - 1;
    printf("string ad %i\n", string_get_size(string));
    int end2 = length2 + start2 - 1;
    char* empty_string = NULL;
    char* result = string_shift(string, start2, shift_way2, end2, empty_string, read);
    return result;
}
bool string_shift2(){
    return false;
}

void string_replace(char* string, char* string2){

    int string_size = string_get_size(string2);
    for(int i = 0; i<=string_size; i++){
        string[i] = string2[i];
    }

}
void string_replace_char(char* string, char* string2){

    int string_size = string_get_size(string2);
    for(int i = 0; i<=string_size; i++){
        string[i] = string2[i];
    }

}
void string_replace_const_char(char* string, const char* string2){

    int string_size = string_get_size_const_char(string2);
    for(int i = 0; i<=string_size; i++){
        string[i] = string2[i];
    }

}

void string_rewrite(char* string, char* string2){
    string_replace(string, string2);
}
void string_rewrite_char(char* string, char* string2){
    string_rewrite(string, string2);
}
void string_rewrite_const_char(char* string, const char* string2){
    string_replace_const_char(string, string2);
}

bool string_append_char(char* string, int* memory_size, char char_for_append){
    int string_size = string_get_size(string);
    if(string_size + 1 >= *memory_size){
        return false;
    }
    string[string_size] = char_for_append;
    string[string_size + 1] = '\0';
    return true;
}
void string_append_string(char* string, int* memory_size, char* string_for_append){
    int string_size = string_get_size_char(string_for_append);
    for(int i = 0; i<string_size; i++){
        string_add(string, string_for_append[i]);
    }
}
void string_append_string_char(char* string, int* memory_size, char* string_for_append){
    string_append_string(string, memory_size, string_for_append);
}
void string_append_string_const_char(char* string, int* memory_size, const char* string_for_append){
    int string_size = string_get_size_const_char(string_for_append);
    for(int i = 0; i<string_size; i++){
        string_add(string, string_for_append[i]);
    }
}

bool string_delete_last_symbol(char* string){
    int string_size = string_get_size(string);
    if(string_size - 1 < 0){
        return false;
    }
    string[string_size - 1] = '\0';
    return true;
}

bool string_multiply_by_symbol(char* string, int* memory_size, char symbol, int count){
    for(int i = 0; i<count; i++){
        string_append_char(string, memory_size, symbol);
    }
    return false;
}
bool string_multiply_by_string(char* string, int* memory_size, char* string_for_append, int count){
    for(int i = 0; i<count; i++){
        string_append_string(string, memory_size, string_for_append);
    }
    return false;
}
bool string_multiply_by_string_char(char* string, int* memory_size, char* string_for_append, int count){
    string_multiply_by_string(string, memory_size, string_for_append, count);
    return false;
}
bool string_multiply_by_string_const_char(char* string, int* memory_size, const char* string_for_append, int count){
    for(int i = 0; i<count; i++){
        string_append_string_const_char(string, memory_size, string_for_append);
    }
    return false;
}

bool string_insert_before(char* string, char* string2, int index){
    string_shift_right(string, index, string_get_size_char(string2));
    string_shift_write(string, index, string_get_size(string2), string2);
    return false;
}
bool string_insert_before_char(char* string, char* string2, int index){
    string_insert_before(string, string2, index);
    return false;
}
bool string_insert_before_const_char(char* string, const char* string2, int index){
    string_shift_right(string, index, string_get_size_const_char(string2));
    string_shift_write_const_char(string, index, string_get_size_const_char(string2), string2);
    return false;
}
bool string_insert_after(char* string, char* string2, int index){
    string_shift_right(string, index + 1, string_get_size_char(string2));
    string_shift_write(string, index + 1, string_get_size(string2), string2);
    return false;
}
bool string_insert_after_char(char* string, char* string2, int index){
    string_insert_after(string, string2, index);
    return false;
}
bool string_insert_after_const_char(char* string, const char* string2, int index){
    string_shift_right(string, index + 1, string_get_size_const_char(string2));
    string_shift_write_const_char(string, index + 1, string_get_size_const_char(string2), string2);
    return false;
}

bool string_find_another_string_char_char(){
    return false;
}
bool string_find_another_string_const_char_char(){
    return false;
}
bool string_find_another_string_char_const_char(){
    return false;
}
bool string_find_another_string_const_char_const_char(){
    return false;
}

bool string_delete_another_string_char_char(){
    return false;
}
bool string_delete_another_string_const_char_char(){
    return false;
}
bool string_delete_another_string_char_const_char(){
    return false;
}
bool string_delete_another_string_const_char_const_char(){
    return false;
}

bool string_insert_string_into_another_string(int startIndex, int endIndex, char* string1, char* string2){
    for(int i = startIndex; i<=endIndex; i++){
        string1[i] = string2[i];
    }
    return false;
}
bool string_insert_string_into_another_string_char(int startIndex, int endIndex, char* string1, char* string2){
    for(int i = startIndex; i<=endIndex; i++){
        string1[i] = string2[i];
    }
    return false;
}
bool string_insert_string_into_another_string_const_char(int startIndex, int endIndex, char* string1, const char* string2){
    for(int i = startIndex; i<=endIndex; i++){
        string1[i] = string2[i];
    }
    return false;
}

bool string_separate_by_symbol(char* string1, char symbol){
    int string_size = string_get_size(string1);
    for(int i = 0; i<string_size; i++){
        if(string1[i] == symbol){
            // do...
        }
    }
    return false;
}
bool string_separate_by_symbol_char(){
    return false;
}
bool string_separate_by_symbol_const_char(){
    return false;
}
bool string_separate_by_string_char_char(){
    return false;
}
bool string_separate_by_string_const_char_char(){
    return false;
}
bool string_separate_by_string_char_const_char(){
    return false;
}
bool string_separate_by_string_const_char_const_char(){
    return false;
}
bool string_separate_by_size_block(){
    return false;
}





void string_print_struct(string_data_type_char* data){

    string_print(data->string);

}

string_data_type_char string_create_struct(int size){

    string_data_type_char data;
    data.string = string_create(size);
    return data;

}
void string_delete_struct(string_data_type_char* data){

    string_delete(data->string);

}

bool string_compare_struct(string_data_type_char* data1, string_data_type_char* data2){
    return string_compare(data1->string, data2->string);
}

bool string_append_struct(string_data_type_char* data, char symbol){
    return string_append_char(data->string, &data->memory_size, symbol);
}

string_data_type_char string_shift_struct(
    string_data_type_char* data1, int start, int counts, 
    int end, string_data_type_char* data2, int action){

    string_shift(data1->string, start, counts, end, data2->string, action);
    return *data1;

}

void string_replace_struct(string_data_type_char* data1, string_data_type_char* data2){
    string_replace_char(data1->string, data2->string);
}

void string_rewrite_struct(string_data_type_char* data1, string_data_type_char* data2){
    string_rewrite_char(data1->string, data2->string);
}


bool string_append_char_struct(string_data_type_char* data, char char_for_append){
    return string_append_char(data->string, &data->memory_size, char_for_append);
}
void string_append_string_struct(string_data_type_char* data1, string_data_type_char* data2){
    string_append_string(data1->string, &data1->memory_size, data2->string);
}


bool string_delete_last_symbol_struct(string_data_type_char* data){
    return string_delete_last_symbol(data->string);
}

