constants = [
    ("int", "MPI_ANY_SOURCE"),
    ("int", "MPI_ANY_TAG"),
    ("int", "MPI_PROC_NULL"),
    ("int", "MPI_ROOT"),

    ("int", "MPI_CART"),
    ("int", "MPI_DIST_GRAPH"),
    ("int", "MPI_GRAPH"),

    # Results of compare operations
    ("int", "MPI_CONGRUENT"),
    ("int", "MPI_IDENT"),
    ("int", "MPI_SIMILAR"),
    ("int", "MPI_UNEQUAL"),

    # Predefined constants
    ("int", "MPI_BSEND_OVERHEAD"),
    ("int", "MPI_KEYVAL_INVALID"),
    ("int", "MPI_UNDEFINED"),

    # Key values
    ("int", "MPI_APPNUM"),
    ("int", "MPI_HOST"),
    ("int", "MPI_IO"),
    ("int", "MPI_LASTUSEDCODE"),
    ("int", "MPI_TAG_UB"),
    ("int", "MPI_UNIVERSE_SIZE"),
    ("int", "MPI_WIN_BASE"),
    ("int", "MPI_WIN_CREATE_FLAVOR"),
    ("int", "MPI_WIN_DISP_UNIT"),
    ("int", "MPI_WIN_MODEL"),
    ("int", "MPI_WIN_SIZE"),
    ("int", "MPI_WTIME_IS_GLOBAL"),

    ("int", "MPI_COMBINER_CONTIGUOUS"),
    ("int", "MPI_COMBINER_DARRAY"),
    ("int", "MPI_COMBINER_DUP"),
    ("int", "MPI_COMBINER_F90_COMPLEX"),
    ("int", "MPI_COMBINER_F90_INTEGER"),
    ("int", "MPI_COMBINER_F90_REAL"),
    ("int", "MPI_COMBINER_HINDEXED"),
    ("int", "MPI_COMBINER_HINDEXED_BLOCK"),
    # ("int", "MPI_COMBINER_HINDEXED_INTEGER"),
    ("int", "MPI_COMBINER_HVECTOR"),
    # ("int", "MPI_COMBINER_HVECTOR_INTEGER"),
    ("int", "MPI_COMBINER_INDEXED"),
    ("int", "MPI_COMBINER_INDEXED_BLOCK"),
    ("int", "MPI_COMBINER_NAMED"),
    ("int", "MPI_COMBINER_RESIZED"),
    ("int", "MPI_COMBINER_STRUCT"),
    # ("int", "MPI_COMBINER_STRUCT_INTEGER"),
    ("int", "MPI_COMBINER_SUBARRAY"),
    ("int", "MPI_COMBINER_VECTOR"),

    ("int", "MPI_COMM_TYPE_SHARED"),

    # File operation constants
    ("int", "MPI_DISTRIBUTE_BLOCK"),
    ("int", "MPI_DISTRIBUTE_CYCLIC"),
    ("int", "MPI_DISTRIBUTE_NONE"),

    ("int", "MPI_ERR_ACCESS"),
    ("int", "MPI_ERR_AMODE"),
    ("int", "MPI_ERR_ARG"),
    ("int", "MPI_ERR_ASSERT"),
    ("int", "MPI_ERR_BAD_FILE"),
    ("int", "MPI_ERR_BASE"),
    ("int", "MPI_ERR_BUFFER"),
    ("int", "MPI_ERR_COMM"),
    ("int", "MPI_ERR_CONVERSION"),
    ("int", "MPI_ERR_COUNT"),
    ("int", "MPI_ERR_DIMS"),
    ("int", "MPI_ERR_DISP"),
    ("int", "MPI_ERR_DUP_DATAREP"),
    ("int", "MPI_ERR_FILE"),
    ("int", "MPI_ERR_FILE_EXISTS"),
    ("int", "MPI_ERR_FILE_IN_USE"),
    ("int", "MPI_ERR_GROUP"),
    ("int", "MPI_ERR_INFO"),
    ("int", "MPI_ERR_INFO_KEY"),
    ("int", "MPI_ERR_INFO_NOKEY"),
    ("int", "MPI_ERR_INFO_VALUE"),
    ("int", "MPI_ERR_INTERN"),
    ("int", "MPI_ERR_IN_STATUS"),
    ("int", "MPI_ERR_IO"),
    ("int", "MPI_ERR_KEYVAL"),
    ("int", "MPI_ERR_LASTCODE"),
    ("int", "MPI_ERR_LOCKTYPE"),
    ("int", "MPI_ERR_NAME"),
    ("int", "MPI_ERR_NOT_SAME"),
    ("int", "MPI_ERR_NO_MEM"),
    ("int", "MPI_ERR_NO_SPACE"),
    ("int", "MPI_ERR_NO_SUCH_FILE"),
    ("int", "MPI_ERR_OP"),
    ("int", "MPI_ERR_OTHER"),
    ("int", "MPI_ERR_PENDING"),
    ("int", "MPI_ERR_PORT"),
    ("int", "MPI_ERR_QUOTA"),
    ("int", "MPI_ERR_RANK"),
    ("int", "MPI_ERR_READ_ONLY"),
    ("int", "MPI_ERR_REQUEST"),
    ("int", "MPI_ERR_RMA_ATTACH"),
    ("int", "MPI_ERR_RMA_CONFLICT"),
    ("int", "MPI_ERR_RMA_FLAVOR"),
    ("int", "MPI_ERR_RMA_RANGE"),
    ("int", "MPI_ERR_RMA_SHARED"),
    ("int", "MPI_ERR_RMA_SYNC"),
    ("int", "MPI_ERR_ROOT"),
    ("int", "MPI_ERR_SERVICE"),
    ("int", "MPI_ERR_SIZE"),
    ("int", "MPI_ERR_SPAWN"),
    ("int", "MPI_ERR_TAG"),
    ("int", "MPI_ERR_TOPOLOGY"),
    ("int", "MPI_ERR_TRUNCATE"),
    ("int", "MPI_ERR_TYPE"),
    ("int", "MPI_ERR_UNKNOWN"),
    ("int", "MPI_ERR_UNSUPPORTED_DATAREP"),
    ("int", "MPI_ERR_UNSUPPORTED_OPERATION"),
    ("int", "MPI_ERR_WIN"),
    ("int", "MPI_SUCCESS"),

    ("int", "MPI_LOCK_EXCLUSIVE"),
    ("int", "MPI_LOCK_SHARED"),

    ("int", "MPI_MODE_APPEND"),
    ("int", "MPI_MODE_CREATE"),
    ("int", "MPI_MODE_DELETE_ON_CLOSE"),
    ("int", "MPI_MODE_EXCL"),
    ("int", "MPI_MODE_NOCHECK"),
    ("int", "MPI_MODE_NOPRECEDE"),
    ("int", "MPI_MODE_NOPUT"),
    ("int", "MPI_MODE_NOSTORE"),
    ("int", "MPI_MODE_NOSUCCEED"),
    ("int", "MPI_MODE_RDONLY"),
    ("int", "MPI_MODE_RDWR"),
    ("int", "MPI_MODE_SEQUENTIAL"),
    ("int", "MPI_MODE_UNIQUE_OPEN"),
    ("int", "MPI_MODE_WRONLY"),

    # File operation constants
    ("int", "MPI_ORDER_C"),
    ("int", "MPI_ORDER_FORTRAN"),

    # File operation constants
    ("int", "MPI_SEEK_CUR"),
    ("int", "MPI_SEEK_END"),
    ("int", "MPI_SEEK_SET"),

    ("int", "MPI_THREAD_SINGLE"),
    ("int", "MPI_THREAD_FUNNELED"),
    ("int", "MPI_THREAD_SERIALIZED"),
    ("int", "MPI_THREAD_MULTIPLE"),

    # File operation constants
    ("int", "MPI_TYPECLASS_COMPLEX"),
    ("int", "MPI_TYPECLASS_INTEGER"),
    ("int", "MPI_TYPECLASS_REAL"),

    ("char **", "MPI_ARGV_NULL"),

    ("char ***", "MPI_ARGVS_NULL"),

    ("int *", "MPI_UNWEIGHTED"),
    ("int *", "MPI_WEIGHTS_EMPTY"),

    ("void *", "MPI_BOTTOM"),

    ("void *", "MPI_IN_PLACE"),

    ("MPI_Comm", "MPI_COMM_NULL"),
    ("MPI_Comm", "MPI_COMM_SELF"),
    ("MPI_Comm", "MPI_COMM_WORLD"),

    ("MPI_Comm_copy_attr_function *", "MPI_COMM_DUP_FN"),
    ("MPI_Comm_copy_attr_function *", "MPI_COMM_NULL_COPY_FN"),

    ("MPI_Comm_delete_attr_function *", "MPI_COMM_NULL_DELETE_FN"),

    ("MPI_Copy_function *", "MPI_NULL_COPY_FN"),

    # ("MPI_Datatype", "MPI_2COMPLEX"),
    # ("MPI_Datatype", "MPI_2DOUBLE"),
    # ("MPI_Datatype", "MPI_2DOUBLE_COMPLEX"),
    ("MPI_Datatype", "MPI_2DOUBLE_PRECISION"),
    # ("MPI_Datatype", "MPI_2FLOAT"),
    ("MPI_Datatype", "MPI_2INT"),
    ("MPI_Datatype", "MPI_2INTEGER"),
    ("MPI_Datatype", "MPI_2REAL"),
    ("MPI_Datatype", "MPI_AINT"),
    ("MPI_Datatype", "MPI_BYTE"),
    ("MPI_Datatype", "MPI_CHAR"),
    ("MPI_Datatype", "MPI_CHARACTER"),
    ("MPI_Datatype", "MPI_COMPLEX"),
    ("MPI_Datatype", "MPI_COMPLEX16"),
    ("MPI_Datatype", "MPI_COMPLEX32"),
    # ("MPI_Datatype", "MPI_COMPLEX4"),
    ("MPI_Datatype", "MPI_COMPLEX8"),
    ("MPI_Datatype", "MPI_COUNT"),
    ("MPI_Datatype", "MPI_CXX_BOOL"),
    ("MPI_Datatype", "MPI_CXX_DOUBLE_COMPLEX"),
    ("MPI_Datatype", "MPI_CXX_FLOAT_COMPLEX"),
    ("MPI_Datatype", "MPI_CXX_LONG_DOUBLE_COMPLEX"),
    ("MPI_Datatype", "MPI_C_BOOL"),
    ("MPI_Datatype", "MPI_C_COMPLEX"),
    ("MPI_Datatype", "MPI_C_DOUBLE_COMPLEX"),
    ("MPI_Datatype", "MPI_C_FLOAT_COMPLEX"),
    ("MPI_Datatype", "MPI_C_LONG_DOUBLE_COMPLEX"),
    ("MPI_Datatype", "MPI_DATATYPE_NULL"),
    ("MPI_Datatype", "MPI_DOUBLE"),
    ("MPI_Datatype", "MPI_DOUBLE_COMPLEX"),
    ("MPI_Datatype", "MPI_DOUBLE_INT"),
    ("MPI_Datatype", "MPI_DOUBLE_PRECISION"),
    ("MPI_Datatype", "MPI_FLOAT"),
    ("MPI_Datatype", "MPI_FLOAT_INT"),
    ("MPI_Datatype", "MPI_INT"),
    ("MPI_Datatype", "MPI_INT16_T"),
    ("MPI_Datatype", "MPI_INT32_T"),
    ("MPI_Datatype", "MPI_INT64_T"),
    ("MPI_Datatype", "MPI_INT8_T"),
    ("MPI_Datatype", "MPI_INTEGER"),
    ("MPI_Datatype", "MPI_INTEGER1"),
    # ("MPI_Datatype", "MPI_INTEGER16"),
    ("MPI_Datatype", "MPI_INTEGER2"),
    ("MPI_Datatype", "MPI_INTEGER4"),
    ("MPI_Datatype", "MPI_INTEGER8"),
    # ("MPI_Datatype", "MPI_LB"),
    ("MPI_Datatype", "MPI_LOGICAL"),
    # ("MPI_Datatype", "MPI_LOGICAL1"),
    # ("MPI_Datatype", "MPI_LOGICAL2"),
    # ("MPI_Datatype", "MPI_LOGICAL4"),
    # ("MPI_Datatype", "MPI_LOGICAL8"),
    ("MPI_Datatype", "MPI_LONG"),
    ("MPI_Datatype", "MPI_LONG_DOUBLE"),
    ("MPI_Datatype", "MPI_LONG_DOUBLE_INT"),
    ("MPI_Datatype", "MPI_LONG_INT"),
    ("MPI_Datatype", "MPI_LONG_LONG"),
    ("MPI_Datatype", "MPI_LONG_LONG_INT"),
    ("MPI_Datatype", "MPI_OFFSET"),
    ("MPI_Datatype", "MPI_PACKED"),
    ("MPI_Datatype", "MPI_REAL"),
    ("MPI_Datatype", "MPI_REAL16"),
    # ("MPI_Datatype", "MPI_REAL2"),
    ("MPI_Datatype", "MPI_REAL4"),
    ("MPI_Datatype", "MPI_REAL8"),
    ("MPI_Datatype", "MPI_SHORT"),
    ("MPI_Datatype", "MPI_SHORT_INT"),
    ("MPI_Datatype", "MPI_SIGNED_CHAR"),
    # ("MPI_Datatype", "MPI_UB"),
    ("MPI_Datatype", "MPI_UINT16_T"),
    ("MPI_Datatype", "MPI_UINT32_T"),
    ("MPI_Datatype", "MPI_UINT64_T"),
    ("MPI_Datatype", "MPI_UINT8_T"),
    ("MPI_Datatype", "MPI_UNSIGNED"),
    ("MPI_Datatype", "MPI_UNSIGNED_CHAR"),
    ("MPI_Datatype", "MPI_UNSIGNED_LONG"),
    ("MPI_Datatype", "MPI_UNSIGNED_LONG_LONG"),
    ("MPI_Datatype", "MPI_UNSIGNED_SHORT"),
    ("MPI_Datatype", "MPI_WCHAR"),

    ("MPI_Delete_function *", "MPI_NULL_DELETE_FN"),

    ("MPI_Errhandler", "MPI_ERRHANDLER_NULL"),
    ("MPI_Errhandler", "MPI_ERRORS_ARE_FATAL"),
    ("MPI_Errhandler", "MPI_ERRORS_RETURN"),

    ("MPI_File", "MPI_FILE_NULL"),

    ("MPI_Group", "MPI_GROUP_EMPTY"),
    ("MPI_Group", "MPI_GROUP_NULL"),

    ("MPI_Info", "MPI_INFO_ENV"),
    ("MPI_Info", "MPI_INFO_NULL"),

    ("MPI_Message", "MPI_MESSAGE_NO_PROC"),
    ("MPI_Message", "MPI_MESSAGE_NULL"),

    # File operation constants
    ("MPI_Offset", "MPI_DISPLACEMENT_CURRENT"),

    ("MPI_Op", "MPI_BAND"),
    ("MPI_Op", "MPI_BOR"),
    ("MPI_Op", "MPI_BXOR"),
    ("MPI_Op", "MPI_LAND"),
    ("MPI_Op", "MPI_LOR"),
    ("MPI_Op", "MPI_LXOR"),
    ("MPI_Op", "MPI_MAX"),
    ("MPI_Op", "MPI_MAXLOC"),
    ("MPI_Op", "MPI_MIN"),
    ("MPI_Op", "MPI_MINLOC"),
    ("MPI_Op", "MPI_NO_OP"),
    ("MPI_Op", "MPI_OP_NULL"),
    ("MPI_Op", "MPI_PROD"),
    ("MPI_Op", "MPI_REPLACE"),
    ("MPI_Op", "MPI_SUM"),

    ("MPI_Request", "MPI_REQUEST_NULL"),

    ("MPI_Status *", "MPI_STATUS_IGNORE"),
    ("MPI_Status *", "MPI_STATUSES_IGNORE"),

    ("MPI_Type_copy_attr_function *", "MPI_TYPE_DUP_FN"),
    ("MPI_Type_copy_attr_function *", "MPI_TYPE_NULL_COPY_FN"),

    ("MPI_Type_delete_attr_function *", "MPI_TYPE_NULL_DELETE_FN"),

    ("MPI_Win", "MPI_WIN_NULL"),

    ("MPI_Win_copy_attr_function *", "MPI_WIN_DUP_FN"),
    ("MPI_Win_copy_attr_function *", "MPI_WIN_NULL_COPY_FN"),

    ("MPI_Win_delete_attr_function *", "MPI_WIN_NULL_DELETE_FN"),
]
